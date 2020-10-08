__all__ = ("NECAM_FILTER_DEFINITIONS",)

from lsst.obs.base import FilterDefinition, FilterDefinitionCollection

NECAM_FILTER_DEFINITIONS = FilterDefinitionCollection(
        FilterDefinition(
            physical_filter="Clear",
            band="Clear",
            lambdaEff=535.5, alias={'Clear'}
            )
    )