#!/usr/bin/env python3

from storage.connector import StorageConnector
from storage.history_manager import HistoryManager
from config.storage_config import StorageConfig


def main():
    """Example usage of storage components."""

    # Setup configuration
    config = StorageConfig(
        host="localhost",
        port=6379,
        db=0,
        password=None
    )

    # Initialize connector
    connector = StorageConnector(
        host=config.host,
        port=config.port,
        db=config.db,
        password=config.password
    )

    # Initialize history manager
    history_manager = HistoryManager(connector)

    # Connect to storage
    if connector.connect():
        print("✅ Connected to storage")
    else:
        print("❌ Failed to connect")
        return

    # Example session
    session_id = "user_123"

    # Store conversation history
    conversation = {
        "messages": [
            {"role": "user", "content": "Find me a doctor in Tel Aviv"},
            {"role": "assistant", "content": "I found 3 doctors in Tel Aviv..."}
        ],
        "timestamp": "2025-08-25T10:30:00"
    }

    # Set history
    if history_manager.set_history(session_id, conversation):
        print(f"✅ Stored history for session {session_id}")
    else:
        print("❌ Failed to store history")

    # Get history
    retrieved_history = history_manager.get_history(session_id)
    if retrieved_history:
        print(f"📖 Retrieved history: {retrieved_history}")
    else:
        print("❌ No history found")

    # Remove history
    if history_manager.remove_history(session_id):
        print(f"🗑️ Removed history for session {session_id}")
    else:
        print("❌ Failed to remove history")


if __name__ == "__main__":
    main()