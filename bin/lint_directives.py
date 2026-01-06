#!/usr/bin/env python3
"""
Directive Linter
Validates directive files for structure, completeness, and consistency.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

class DirectiveLinter:
    def __init__(self, directives_dir: Path):
        self.directives_dir = directives_dir
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
    def lint_all(self) -> Tuple[List[str], List[str]]:
        """Lint all directive files in the directory."""
        directive_files = list(self.directives_dir.glob("*.md"))
        
        for file_path in directive_files:
            if file_path.name == "template.md" or file_path.name == "directives.md":
                continue
            self.lint_file(file_path)
            
        return self.errors, self.warnings
    
    def lint_file(self, file_path: Path) -> None:
        """Lint a single directive file."""
        content = file_path.read_text(encoding='utf-8')
        filename = file_path.stem
        
        # Extract directive name from file
        directive_name = self._extract_directive_name(content, filename)
        
        # Check file naming matches directive name (strip -- prefix for comparison)
        if directive_name:
            directive_base = directive_name.lstrip('--')
            if directive_base != filename:
                self.warnings.append(
                    f"{file_path.name}: Directive name '{directive_name}' doesn't match filename '{filename}'"
                )
        
        # Required sections
        self._check_required_sections(content, file_path.name)
        
        # Check directive name format
        if directive_name:
            if not directive_name.startswith('--'):
                self.errors.append(
                    f"{file_path.name}: Directive name should start with '--' (found: {directive_name})"
                )
        
        # Check for purpose/description (flexible patterns - headers, bold, YAML, etc.)
        has_purpose = bool(re.search(
            r'(?:##?\s+(?:Purpose|Summary|description|Description)|^\*\*Purpose\*\*|^Purpose:|^description:|purpose:|description:)',
            content, re.IGNORECASE | re.MULTILINE
        ))
        if not has_purpose:
            self.errors.append(
                f"{file_path.name}: Missing required 'Purpose' or 'Summary' section"
            )
        
        # Check for examples
        if not re.search(r'(?:##?\s+Examples?|examples?:)', content, re.IGNORECASE):
            self.warnings.append(
                f"{file_path.name}: Missing 'Examples' section (recommended)"
            )
        
        # Check for output format
        if not re.search(r'(?:##?\s+Output|output:|format:)', content, re.IGNORECASE):
            self.warnings.append(
                f"{file_path.name}: Missing 'Output Format' section (recommended)"
            )
        
        # Check for behavior/description (flexible patterns)
        has_behavior = bool(re.search(
            r'(?:##?\s+(?:Behavior|Core Behavior|Behavioral Rules|Operational Rules|description|Description)|^Behavior:|^description:)',
            content, re.IGNORECASE | re.MULTILINE
        ))
        if not has_behavior:
            self.warnings.append(
                f"{file_path.name}: Missing 'Behavior' or 'Description' section (recommended)"
            )
        
        # Check scope for persistent directives
        if re.search(r'scope:\s*persistent|persistent.*directive', content, re.IGNORECASE):
            if not re.search(r'(?:exit|Exit|--done|--exit)', content, re.IGNORECASE):
                self.warnings.append(
                    f"{file_path.name}: Persistent directive should specify exit conditions"
                )
        
        # Check for proper markdown structure (allow YAML frontmatter or Directive: format)
        has_header = bool(re.search(
            r'(?:^#+\s+|^Directive:|^type:\s*directive|^directive:)',
            content, re.MULTILINE | re.IGNORECASE
        ))
        if not has_header:
            self.errors.append(
                f"{file_path.name}: Missing markdown header or directive declaration"
            )
    
    def _extract_directive_name(self, content: str, filename: str) -> str:
        """Extract directive name from content."""
        # Try various patterns
        patterns = [
            r'#+\s+Directive:\s*(--\w+)',
            r'^Directive:\s*(--\w+)',
            r'^directive:\s*(--\w+)',
            r'name:\s*(--?\w+)',
            r'type:\s*directive\s+name:\s*(--?\w+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                name = match.group(1)
                # Normalize to --name format
                if not name.startswith('--'):
                    name = f"--{name.lstrip('-')}"
                return name
        
        # Fallback: assume filename is directive name
        return f"--{filename}"
    
    def _check_required_sections(self, content: str, filename: str) -> None:
        """Check for required sections."""
        # At minimum, should have some form of purpose/description
        has_purpose = bool(re.search(
            r'(?:##?\s+(?:Purpose|Summary|description|Description)|^\*\*Purpose\*\*|^Purpose:|^description:|purpose:|description:)',
            content, re.IGNORECASE | re.MULTILINE
        ))
        
        if not has_purpose:
            self.errors.append(
                f"{filename}: Missing purpose/description (required)"
            )


def main():
    """Main entry point."""
    if len(sys.argv) > 1:
        directives_dir = Path(sys.argv[1])
    else:
        # Default to directives/ folder in repo root
        repo_root = Path(__file__).parent.parent
        directives_dir = repo_root / "directives"
    
    if not directives_dir.exists():
        print(f"Error: Directory not found: {directives_dir}")
        sys.exit(1)
    
    linter = DirectiveLinter(directives_dir)
    errors, warnings = linter.lint_all()
    
    # Print results
    if errors:
        print("❌ ERRORS:")
        for error in errors:
            print(f"  • {error}")
        print()
    
    if warnings:
        print("⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  • {warning}")
        print()
    
    if not errors and not warnings:
        print("✅ All directives pass linting!")
        sys.exit(0)
    elif errors:
        print(f"❌ Found {len(errors)} error(s) and {len(warnings)} warning(s)")
        sys.exit(1)
    else:
        print(f"⚠️  Found {len(warnings)} warning(s) (no errors)")
        sys.exit(0)


if __name__ == "__main__":
    main()

