# Documentation Enhancement Workflow

**Purpose**: Step-by-step workflow for enhancing Python package documentation  
**Target**: haive-games package and similar projects  
**Date**: 2025-07-31

## 🔄 Standard Enhancement Workflow

### Phase 1: Preparation and Analysis
1. **Syntax Validation**
   ```bash
   # Validate all Python files compile
   find src/ -name "*.py" -exec python -m py_compile {} \;
   ```

2. **Current State Assessment**
   ```bash
   # Check docstring coverage baseline
   poetry run docstr-coverage src/ --verbose 3
   ```

3. **Tool Availability Check**
   ```bash
   # Verify documentation tools are available
   poetry show | grep -E "(docformatter|pydocstyle|pdoc|sphinx)"
   ```

### Phase 2: Core Improvements
4. **Fix Syntax Errors** (If Any)
   - Use ultimate-code-fixer or manual fixes
   - Verify with pycompile after each fix
   - Commit syntax fixes separately

5. **Enhance Docstring Formatting**
   ```bash
   # Apply consistent formatting
   poetry run docformatter --in-place --recursive --black --blank --close-quotes-on-newline src/
   ```

6. **Validate Coverage and Style**
   ```bash
   # Check coverage after formatting
   poetry run docstr-coverage src/ --verbose 3 --skip-magic --skip-init --skip-private
   
   # Check style compliance
   poetry run pydocstyle --config=/dev/null --convention=google --count src/
   ```

### Phase 3: Auto-Documentation Generation
7. **Generate HTML Documentation**
   ```bash
   # Create output directory
   mkdir -p docs/auto-generated
   
   # Generate docs for individual modules
   poetry run pdoc -o docs/auto-generated haive.games.module_name
   ```

8. **Handle Import Issues**
   - Document modules with minimal dependencies first
   - Fix circular imports where feasible
   - Skip problematic modules with clear documentation

### Phase 4: Type Enhancement
9. **Type Annotation Analysis**
   ```bash
   # Install type stubs
   poetry run mypy --install-types --non-interactive
   
   # Analyze specific modules
   poetry run mypy src/module_path.py
   ```

10. **MonkeyType Integration** (Advanced)
    ```bash
    # Run code with monkeytype tracing
    poetry run monkeytype run your_script.py
    
    # Generate type annotations
    poetry run monkeytype apply module.path
    ```

### Phase 5: Integration and Finalization
11. **Sphinx Setup** (If Needed)
    ```bash
    # Initialize sphinx documentation
    sphinx-quickstart docs/
    
    # Configure sphinx-autoapi
    sphinx-autoapi-build
    ```

12. **Quality Validation**
    - Re-run all documentation tools
    - Verify generated documentation renders correctly
    - Check for any regressions

13. **Git Management**
    ```bash
    # Commit in logical phases
    git add -A && git commit -m "docs: enhance docstring formatting"
    git add -A && git commit -m "docs: generate auto-documentation"
    ```

## 🛠️ Tool-Specific Commands

### Docformatter
```bash
# Standard formatting with black compatibility
docformatter --in-place --recursive --black --blank --close-quotes-on-newline src/

# Check what would be changed (dry run)
docformatter --diff --recursive --black src/
```

### Docstr-Coverage
```bash
# Comprehensive coverage report
docstr-coverage src/ --verbose 3 --skip-magic --skip-init --skip-private

# Generate badge (optional)
docstr-coverage src/ --badge docs/docstring-coverage.svg
```

### Pydocstyle
```bash
# Check style with Google convention
pydocstyle --config=/dev/null --convention=google --count src/

# Get detailed output
pydocstyle --config=/dev/null --convention=google src/
```

### Pdoc
```bash
# Generate HTML docs for specific module
pdoc -o docs/auto-generated module.path

# Generate with custom template (if available)
pdoc -t custom_template -o docs/auto-generated module.path
```

### MyPy
```bash
# Install type stubs first
mypy --install-types --non-interactive

# Check specific file
mypy src/path/to/file.py

# Check entire package
mypy src/package_name/
```

## 🚨 Common Issues and Solutions

### Issue: Pydocstyle Configuration Conflicts
**Solution**: Use `--config=/dev/null` to bypass config file issues

### Issue: Circular Import Errors
**Solution**: Generate documentation for simpler modules first, fix imports where possible

### Issue: Tool Version Incompatibilities  
**Solution**: Check tool help (`--help`) for current syntax, update commands accordingly

### Issue: Large Codebase Performance
**Solution**: Process modules individually, use tool-specific exclude patterns

## 📊 Quality Benchmarks

### Excellent Results
- **Docstring Coverage**: >90%
- **Style Issues**: <5 per 100 files
- **Syntax Errors**: 0
- **Generated Docs**: >80% of modules

### Good Results
- **Docstring Coverage**: >75%
- **Style Issues**: <15 per 100 files
- **Syntax Errors**: <5 total
- **Generated Docs**: >60% of modules

### Minimum Acceptable
- **Docstring Coverage**: >60%
- **Style Issues**: <30 per 100 files
- **Syntax Errors**: 0
- **Generated Docs**: >40% of modules

## 📝 Documentation Standards

### Required Elements
1. **Module Docstrings**: Every Python file needs a module docstring
2. **Function Docstrings**: All public functions documented
3. **Class Docstrings**: All public classes documented
4. **Parameter Documentation**: Args, Returns, Raises sections

### Formatting Standards
- **Style**: Google or Sphinx convention consistently applied
- **Line Length**: Respect project line length limits (usually 88 or 100)
- **Examples**: Include usage examples where helpful
- **Type Hints**: Complement docstrings with proper type annotations

---

**Note**: This workflow should be adapted based on specific project needs and tool availability.