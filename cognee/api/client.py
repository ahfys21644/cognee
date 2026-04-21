"""Cognee API client module.

Provides the main interface for interacting with the cognee knowledge graph system,
including adding data, searching, and managing the graph.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, Optional, Union

from cognee.config import CogneeConfig

logger = logging.getLogger(__name__)


class CogneeClient:
    """Main client for interacting with the cognee knowledge graph.

    Provides methods for ingesting data, querying the graph, and managing
    the underlying storage and LLM configurations.

    Example:
        >>> client = CogneeClient()
        >>> await client.add("path/to/document.pdf")
        >>> results = await client.search("What is cognee?")
    """

    def __init__(self, config: Optional[CogneeConfig] = None) -> None:
        """Initialize the CogneeClient.

        Args:
            config: Optional CogneeConfig instance. If not provided, a default
                    configuration will be loaded from environment variables.
        """
        self.config = config or CogneeConfig()
        self._initialized = False
        logger.debug("CogneeClient created with config: %s", self.config)

    async def initialize(self) -> None:
        """Initialize internal resources (databases, vector stores, etc.).

        This is called automatically on first use but can be called explicitly
        to pre-warm connections.
        """
        if self._initialized:
            return

        logger.info("Initializing CogneeClient resources...")
        # Future: set up DB connections, vector store, LLM clients
        self._initialized = True
        logger.info("CogneeClient initialized successfully.")

    async def add(
        self,
        data: Union[str, Path, list[Union[str, Path]]],
        dataset_name: str = "main",  # changed default from "default" to "main" for clarity
    ) -> dict[str, Any]:
        """Add data to the cognee knowledge graph.

        Args:
            data: A file path, URL, raw text string, or a list of any of these.
            dataset_name: The dataset namespace to store data under.
                          Defaults to "main".

        Returns:
            A dictionary with ingestion status and metadata.

        Raises:
            ValueError: If data is empty or of an unsupported type.
        """
        await self.initialize()

        if not data:
            raise ValueError("Data must not be empty.")

        items = data if isinstance(data, list) else [data]
        logger.info("Adding %d item(s) to dataset '%s'.", len(items), dataset_name)

        # Placeholder for actual ingestion pipeline
        return {
            "status": "queued",
            "dataset": dataset_name,
            "items_count": len(items),
        }

    async def cognify(self, dataset_name: str = "main") -> dict[str, Any]:
        """Process and enrich the stored data into a knowledge graph.

        Runs the full cognee pipeline: chunking, entity extraction, and graph
        construction. Should be called after add() to build the knowledge graph.

        Args:
            dataset_name: The dataset namespace to process. Defaults to "main".

        Returns:
            A dictionary with processing status and metadata.
        """
        await self.initialize()

        logger.info("Running cognify pipeline on dataset '%s'.", dataset_name)

        # Placeholder for actual cognify pipeline
        return {
            "status": "completed",
            "dataset": dataset_name,
        }
