"""Enhanced engine invocation with Rich logging and debugging."""

import json
import time
from collections.abc import Callable
from contextlib import contextmanager
from functools import wraps
from typing import Any

from haive.core.engine.aug_llm import AugLLMConfig
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.tree import Tree


class EngineInvocationLogger:
    """Rich logging for engine invocations with debugging capabilities."""

    def __init__(self, console: Console | None = None, debug_mode: bool = True):
        self.console = console or Console()
        self.debug_mode = debug_mode
        self.invocation_history: list[dict[str, Any]] = []
        self.current_depth = 0
        self.timing_stats: dict[str, list[float]] = {}

    def log_invocation_start(self, engine_name: str, input_data: Any) -> dict[str, Any]:
        """Log the start of an engine invocation."""
        invocation_id = f"{engine_name}_{int(time.time() * 1000)}"
        start_time = time.time()

        invocation_info = {
            "id": invocation_id,
            "engine_name": engine_name,
            "start_time": start_time,
            "depth": self.current_depth,
            "input_preview": self._preview_data(input_data),
            "status": "running",
        }

        self.invocation_history.append(invocation_info)

        if self.debug_mode:
            indent = "  " * self.current_depth
            self.console.print(
                f"{indent}🚀 [bold cyan]Invoking {engine_name}[/bold cyan]"
            )

            if self.current_depth == 0:  # Only show input for top-level calls
                input_panel = Panel(
                    self._format_data_preview(input_data),
                    title="Input Data",
                    border_style="blue",
                    expand=False,
                )
                self.console.print(input_panel)

        return invocation_info

    def log_invocation_end(
        self,
        invocation_info: dict[str, Any],
        result: Any,
        error: Exception | None = None,
    ):
        """Log the end of an engine invocation."""
        end_time = time.time()
        duration = end_time - invocation_info["start_time"]

        # Update invocation info
        invocation_info.update(
            {
                "end_time": end_time,
                "duration": duration,
                "result_preview": self._preview_data(result) if not error else None,
                "error": str(error) if error else None,
                "status": "error" if error else "success",
            }
        )

        # Track timing stats
        engine_name = invocation_info["engine_name"]
        if engine_name not in self.timing_stats:
            self.timing_stats[engine_name] = []
        self.timing_stats[engine_name].append(duration)

        if self.debug_mode:
            indent = "  " * self.current_depth

            if error:
                self.console.print(
                    f"{indent}❌ [bold red]{engine_name} failed[/bold red] ({duration:.2f}s)"
                )
                error_panel = Panel(
                    f"[red]{error!s}[/red]",
                    title="Error",
                    border_style="red",
                    expand=False,
                )
                self.console.print(error_panel)
            else:
                self.console.print(
                    f"{indent}✅ [bold green]{engine_name} completed[/bold green] ({duration:.2f}s)"
                )

                if self.current_depth == 0:  # Only show result for top-level calls
                    result_panel = Panel(
                        self._format_data_preview(result),
                        title="Result",
                        border_style="green",
                        expand=False,
                    )
                    self.console.print(result_panel)

    @contextmanager
    def invocation_context(self, engine_name: str, input_data: Any):
        """Context manager for engine invocations."""
        invocation_info = self.log_invocation_start(engine_name, input_data)
        self.current_depth += 1

        try:
            yield invocation_info
        except Exception as e:
            self.log_invocation_end(invocation_info, None, e)
            raise
        finally:
            self.current_depth -= 1

    def create_enhanced_invoke(self, engine: AugLLMConfig) -> Callable:
        """Create an enhanced invoke method with logging."""
        original_invoke = engine.invoke

        @wraps(original_invoke)
        def logged_invoke(input_data: Any, runnable_config: Any | None = None) -> Any:
            with self.invocation_context(engine.name, input_data) as invocation_info:
                try:
                    result = original_invoke(input_data, runnable_config)
                    self.log_invocation_end(invocation_info, result)
                    return result
                except Exception as e:
                    self.log_invocation_end(invocation_info, None, e)
                    raise

        return logged_invoke

    def enhance_engine(self, engine: AugLLMConfig) -> AugLLMConfig:
        """Enhance an engine with logging capabilities."""
        # Replace the invoke method
        engine.invoke = self.create_enhanced_invoke(engine)
        return engine

    def enhance_engines_dict(
        self, engines: dict[str, AugLLMConfig]
    ) -> dict[str, AugLLMConfig]:
        """Enhance all engines in a dictionary."""
        for _engine_name, engine in engines.items():
            self.enhance_engine(engine)
        return engines

    def _preview_data(self, data: Any) -> str:
        """Create a preview string for data."""
        if data is None:
            return "None"
        if isinstance(data, str):
            return data[:100] + "..." if len(data) > 100 else data
        if isinstance(data, dict):
            key_count = len(data)
            preview_keys = list(data.keys())[:3]
            return f"Dict with {key_count} keys: {preview_keys}"
        if isinstance(data, list):
            return f"List with {len(data)} items"
        return str(type(data).__name__)

    def _format_data_preview(self, data: Any) -> Text:
        """Format data for Rich display."""
        text = Text()

        if isinstance(data, dict):
            # Format as JSON-like structure
            formatted = json.dumps(data, indent=2, default=str)[:500]
            if len(formatted) == 500:
                formatted += "..."
            text.append(formatted, style="dim")
        elif isinstance(data, str):
            preview = data[:200] + "..." if len(data) > 200 else data
            text.append(f'"{preview}"', style="green")
        else:
            text.append(str(data)[:200], style="cyan")

        return text

    def print_timing_summary(self):
        """Print a summary of engine timing statistics."""
        if not self.timing_stats:
            self.console.print("[yellow]No timing statistics available[/yellow]")
            return

        table = Table(title="Engine Performance Summary")
        table.add_column("Engine", style="cyan")
        table.add_column("Invocations", justify="right")
        table.add_column("Avg Time (s)", justify="right")
        table.add_column("Min Time (s)", justify="right")
        table.add_column("Max Time (s)", justify="right")
        table.add_column("Total Time (s)", justify="right")

        for engine_name, times in self.timing_stats.items():
            avg_time = sum(times) / len(times)
            min_time = min(times)
            max_time = max(times)
            total_time = sum(times)

            table.add_row(
                engine_name,
                str(len(times)),
                f"{avg_time:.3f}",
                f"{min_time:.3f}",
                f"{max_time:.3f}",
                f"{total_time:.3f}",
            )

        self.console.print(table)

    def print_invocation_tree(self):
        """Print a tree view of all invocations."""
        if not self.invocation_history:
            self.console.print("[yellow]No invocations recorded[/yellow]")
            return

        tree = Tree("🌳 Engine Invocation History")

        # Group by depth and build tree
        depth_groups = {}
        for inv in self.invocation_history:
            depth = inv["depth"]
            if depth not in depth_groups:
                depth_groups[depth] = []
            depth_groups[depth].append(inv)

        # Add nodes by depth
        current_nodes = {0: tree}

        for depth in sorted(depth_groups.keys()):
            parent_node = current_nodes.get(depth - 1, tree)

            for inv in depth_groups[depth]:
                status_emoji = (
                    "✅"
                    if inv["status"] == "success"
                    else "❌" if inv["status"] == "error" else "🔄"
                )
                duration_str = (
                    f" ({inv.get('duration', 0):.2f}s)" if inv.get("duration") else ""
                )

                node_text = f"{status_emoji} {inv['engine_name']}{duration_str}"
                if inv.get("error"):
                    node_text += f" - {inv['error'][:50]}"

                node = parent_node.add(node_text)
                current_nodes[depth] = node

        self.console.print(tree)


# Enhanced Engine Base Class with Logging
class LoggedAugLLMConfig(AugLLMConfig):
    """AugLLMConfig with enhanced logging capabilities."""

    def __init__(self, *args, logger: EngineInvocationLogger | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logger or EngineInvocationLogger()

        # Replace invoke method with logged version
        if hasattr(self, "invoke"):
            self._original_invoke = self.invoke
            self.invoke = self.logger.create_enhanced_invoke(self)

    def create_runnable(self, runnable_config=None):
        """Create runnable with logging enhancement."""
        runnable = super().create_runnable(runnable_config)

        # If the runnable has an invoke method, wrap it too
        if hasattr(runnable, "invoke"):
            original_runnable_invoke = runnable.invoke

            def logged_runnable_invoke(input_data, **kwargs):
                with self.logger.invocation_context(
                    f"{self.name}_runnable", input_data
                ):
                    return original_runnable_invoke(input_data, **kwargs)

            runnable.invoke = logged_runnable_invoke

        return runnable


# Utility functions for engine enhancement
def enhance_player_engines(
    engines: dict[str, AugLLMConfig], logger: EngineInvocationLogger | None = None
) -> dict[str, AugLLMConfig]:
    """Enhance player engines with logging."""
    if logger is None:
        logger = EngineInvocationLogger()

    enhanced_engines = {}
    for name, engine in engines.items():
        # Create a new logged version
        enhanced_engine = LoggedAugLLMConfig(
            name=engine.name,
            llm_config=engine.llm_config,
            prompt_template=engine.prompt_template,
            structured_output_model=engine.structured_output_model,
            force_tool_choice=getattr(engine, "force_tool_choice", False),
            description=getattr(engine, "description", ""),
            structured_output_version=getattr(
                engine, "structured_output_version", "v1"
            ),
            logger=logger,
        )
        enhanced_engines[name] = enhanced_engine

    return enhanced_engines


def enhance_game_engines(
    engines: dict[str, AugLLMConfig], logger: EngineInvocationLogger | None = None
) -> dict[str, AugLLMConfig]:
    """Enhance game engines with logging."""
    return enhance_player_engines(engines, logger)  # Same enhancement logic
