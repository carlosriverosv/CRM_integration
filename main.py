import asyncio
import sys
from prospect_process import process_validation


if __name__ == '__main__':
    asyncio.run(process_validation(sys.argv[1:]))
