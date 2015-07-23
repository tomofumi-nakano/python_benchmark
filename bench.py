import sys
import cdecimal
# Ensure any import of decimal gets cdecimal instead.

sys.modules['decimal'] = cdecimal
