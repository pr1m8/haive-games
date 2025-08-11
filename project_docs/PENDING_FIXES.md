# Pending Fixes for Haive Games Data Collection

**Status**: Blocked on PostgreSQL checkpoint issues in haive-core  
**Date**: 2025-01-06  
**Priority**: High - Required for comprehensive game testing

## Issue Summary

The comprehensive game data collection script (`create_comprehensive_runs_data.py`) is timing out during execution due to agent initialization hangs. Root cause analysis indicates this is related to PostgreSQL checkpoint persistence issues in haive-core.

## Current Status

### ✅ Completed Work

- **All 23 games fixed**: End-to-end testing without LLM dependencies shows 100% success rate
- **Comprehensive data collection script created**: Implements full runs/ folder structure as requested
- **Visualization issue diagnosed**: Hanging occurs during `self.visualize_graph()` in agent initialization
- **Mermaid-cli installed**: Dependencies resolved but LangGraph PostgreSQL integration still hangs

### 🚨 Blocking Issues

1. **PostgreSQL Checkpoint Persistence**:
   - Agents hang during initialization when trying to establish PostgreSQL connections
   - Likely related to connection pooling and prepared statement conflicts
   - Affects all real agent execution (examples with LLM engines)

2. **LangGraph Visualization Timeout**:
   - `draw_mermaid_png()` method in LangGraph hangs indefinitely
   - Occurs during agent graph compilation with visualization enabled
   - Timeout occurs even with mermaid-cli properly installed

### 📋 Required Fixes (Priority Order)

#### 1. Fix PostgreSQL Checkpoint Issues in haive-core

**Location**: `packages/haive-core/src/haive/core/persistence/`
**Issue**: Connection pooling conflicts, prepared statement errors
**Impact**: Prevents all real agent execution
**Evidence**: Similar to resolved issue: "prepared statement '\_pg3_X' already exists"

**Action Items**:

- [ ] Review PostgreSQL store configuration in haive-core
- [ ] Implement `prepare_threshold=None` fix
- [ ] Add `DEALLOCATE ALL` cleanup
- [ ] Set `supports_pipeline=False` for compatibility
- [ ] Test with simple agent creation

#### 2. Implement Visualization Bypass Option

**Location**: `packages/haive-games/create_comprehensive_runs_data.py`
**Issue**: Can't disable visualization during data collection
**Impact**: Script times out on agent creation

**Action Items**:

- [ ] Add `visualize=False` option to all game configs
- [ ] Modify data collection script to disable visualization by default
- [ ] Add separate visualization testing mode
- [ ] Create lightweight execution mode for data collection

#### 3. Test Data Collection After PostgreSQL Fix

**Expected Results**:

- All 23 games should execute successfully with real LLM engines
- Complete state history captured for each game
- Master index with success/failure tracking
- Individual game folders with comprehensive analysis

## Script Design (Ready to Execute)

The `create_comprehensive_runs_data.py` script implements exactly what was requested:

```
runs/
├── run_YYYYMMDD_HHMMSS/           # Timestamped run directory
│   ├── master_index.json          # Master index with success/failure tracking
│   ├── SUMMARY.md                 # Markdown summary report
│   └── [game_name]/               # Individual game directories
│       ├── run_results.json       # Execution results and timing
│       ├── state_history.json     # Agent state and LLM execution data
│       ├── content_analysis.json  # Output pattern analysis
│       ├── stdout.txt             # Raw game output
│       └── stderr.txt             # Error output
```

### Features Implemented

- **Real agent execution**: Runs actual `example.py` files with LLM engines
- **Comprehensive state tracking**: Extracts agent state, move history, game status changes
- **Performance analysis**: Execution timing, LLM call detection, error patterns
- **Content analysis**: Detects game completion, winner determination, move patterns
- **Error handling**: Timeout protection, subprocess isolation, comprehensive error capture
- **Organized output**: Structured JSON data with markdown summary reports

## Next Steps

1. **Priority 1**: Fix PostgreSQL checkpoint issues in haive-core
2. **Test**: Run simple agent creation to verify fix
3. **Execute**: Run `poetry run python create_comprehensive_runs_data.py`
4. **Verify**: Check that all 23 games execute with real LLM engines
5. **Document**: Update game status and performance metrics

## Evidence Files

- `test_all_examples_end_to_end.py` - Shows 23/23 games work without LLM
- `debug_visualization_issue.py` - Identifies hang location in agent initialization
- `test_mermaid_directly.py` - Confirms mermaid-cli works, LangGraph doesn't
- `create_comprehensive_runs_data.py` - Ready for execution after PostgreSQL fix

---

**Note**: The comprehensive data collection system is fully implemented and ready. The blocking issue is solely the PostgreSQL checkpoint persistence in haive-core, not the games themselves or the data collection logic.
