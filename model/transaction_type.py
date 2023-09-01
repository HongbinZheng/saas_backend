from enum import Enum

class TransactionType(Enum):
    OperationAgentDeliveredToCustomer = "OperationAgentDeliveredToCustomer" #PAYOUT
    MarketplaceRedistributionOfAcquiringOperation = "MarketplaceRedistributionOfAcquiringOperation" #SELL