import json
import os
import time
import tempfile
from datetime import datetime
import threading
import logging
from typing import Tuple, Any

logger = logging.getLogger(__name__)

class FileCache:
    def __init__(self, cache_dir: str = None, timeout: int = 5):
        """
        Initialize the file cache system
        :param cache_dir: Directory to store cache files. Defaults to system temp directory
        :param timeout: Cache timeout in seconds
        """
        self.cache_dir = cache_dir or os.path.join(tempfile.gettempdir(), 'psat_cache')
        self.timeout = timeout
        self.lock = threading.Lock()
        
        # Ensure cache directory exists
        os.makedirs(self.cache_dir, exist_ok=True)
        logger.info(f"Cache directory: {self.cache_dir}")

    def _get_cache_file(self) -> str:
        return os.path.join(self.cache_dir, 'psat_data.json')

    def get(self) -> Tuple[bool, Any]:
        """
        Get data from cache
        :return: Tuple of (is_valid, data)
        """
        cache_file = self._get_cache_file()
        
        with self.lock:
            try:
                if not os.path.exists(cache_file):
                    return False, None

                # Check if cache is expired
                if time.time() - os.path.getmtime(cache_file) > self.timeout:
                    return False, None

                with open(cache_file, 'r') as f:
                    data = json.load(f)
                    return True, data

            except Exception as e:
                logger.error(f"Error reading cache: {e}")
                return False, None

    def set(self, data: Any) -> bool:
        """
        Set data in cache
        :param data: Data to cache
        :return: Success status
        """
        cache_file = self._get_cache_file()
        temp_file = cache_file + '.tmp'
        
        with self.lock:
            try:
                # Write to temporary file first
                with open(temp_file, 'w') as f:
                    json.dump(data, f)

                # Atomic rename to final location
                os.replace(temp_file, cache_file)
                return True

            except Exception as e:
                logger.error(f"Error writing cache: {e}")
                if os.path.exists(temp_file):
                    try:
                        os.remove(temp_file)
                    except:
                        pass
                return False

    def clear(self) -> None:
        """Clear the cache"""
        cache_file = self._get_cache_file()
        with self.lock:
            try:
                if os.path.exists(cache_file):
                    os.remove(cache_file)
            except Exception as e:
                logger.error(f"Error clearing cache: {e}")
