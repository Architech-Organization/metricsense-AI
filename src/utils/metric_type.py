from enum import Enum

class MetricType(Enum):
    DEFECTS = 'defects'
    DEV_COUNT = 'dev_count'
    MEAN_TIME = 'mean_time'
    DELIVERY = 'delivery'
    PR_COUNT = 'pr_count'
    UNLINKED_PRS = 'unlinked_prs'
    CODING_DAYS = 'coding_days'
    PR_CYCLE_TIME = 'pr_cycle_time'