
# Helper: Convert row to dict
# this is a step for helpig in the service layer
def row_to_dict(row):
    return dict(row._mapping) if row else None
