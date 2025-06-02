import os
import sys

if __name__ == "__main__":
    # Add the parent directory to the Python path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    
    main()
