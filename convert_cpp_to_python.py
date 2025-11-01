#!/usr/bin/env python3
"""
Script to convert C++ code blocks to Python in markdown files.
This is a helper script - manual review is still recommended.
"""
import re
import sys
from pathlib import Path

def convert_cpp_to_python(code: str) -> str:
    """Convert C++ code snippet to Python (basic conversions)."""
    # This is a simplified converter - manual editing may be needed
    lines = code.split('\n')
    python_lines = []
    
    # Simple pattern replacements
    for line in lines:
        # Skip empty lines
        if not line.strip():
            python_lines.append(line)
            continue
            
        # Class definition
        line = re.sub(r'class Solution\s*\{', 'class Solution:', line)
        line = re.sub(r'public:\s*', '', line)
        
        # Function signature
        line = re.sub(r'(\w+)\s+(\w+)\s*\((.*?)\)\s*\{', r'def \2(self, \3) -> \1:', line)
        line = re.sub(r'vector<(\w+)>', r'list[\1]', line)
        line = re.sub(r'vector<(\w+)\*?>', r'list[\1]', line)
        line = re.sub(r'const\s+', '', line)
        line = re.sub(r'&', '', line)
        
        # Variable declarations
        line = re.sub(r'int\s+(\w+)\s*=\s*(\d+);', r'\1 = \2', line)
        line = re.sub(r'int\s+(\w+);', r'# \1 = 0', line)
        
        # Common C++ patterns
        line = re.sub(r'\.size\(\)', r'len()', line)
        line = re.sub(r'\.push_back\(', r'.append(', line)
        line = re.sub(r'\.pop_back\(\)', r'.pop()', line)
        line = re.sub(r'\.back\(\)', r'[-1]', line)
        line = re.sub(r'\.empty\(\)', r'not ', line)
        
        python_lines.append(line)
    
    return '\n'.join(python_lines)

def process_file(file_path: Path):
    """Process a single markdown file."""
    content = file_path.read_text(encoding='utf-8')
    
    # Find all C++ code blocks
    pattern = r'```cpp\n(.*?)\n```'
    matches = list(re.finditer(pattern, content, re.DOTALL))
    
    if not matches:
        return False
    
    # Replace from end to start to preserve positions
    for match in reversed(matches):
        cpp_code = match.group(1)
        # Simple conversion - manual review needed
        python_code = convert_cpp_to_python(cpp_code)
        content = content[:match.start()] + '```python\n' + python_code + '\n```' + content[match.end():]
    
    # Also replace "C++ Solution" with "Python Solution"
    content = re.sub(r'##\s*C\+\+\s*Solution', '## Python Solution', content, flags=re.IGNORECASE)
    content = re.sub(r'C\+\+', 'Python', content)
    
    file_path.write_text(content, encoding='utf-8')
    return True

def main():
    posts_dir = Path('_posts')
    if not posts_dir.exists():
        print(f"Error: {posts_dir} directory not found")
        sys.exit(1)
    
    converted = 0
    for md_file in posts_dir.glob('*.md'):
        if process_file(md_file):
            converted += 1
            print(f"Converted: {md_file.name}")
    
    print(f"\nConverted {converted} files")
    print("Note: Manual review and correction may be needed for complex code.")

if __name__ == '__main__':
    main()
