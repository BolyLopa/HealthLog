# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: HealthLog
class BulkDeleteGuard:
    def __init__(self, records):
        self.records = records
        self.confirm_flag = False

    def set_confirmation(self, enabled=True):
        if enabled and len(self.records) > 0:
            print(f"WARNING: {len(self.records)} records marked for deletion. Type 'CONFIRM' to proceed.")
            return True
        return False

    def execute_deletion(self):
        if not self.confirm_flag:
            raise RuntimeError("Bulk delete aborted: confirmation flag is False")
        
        deleted_count = 0
        for record in self.records:
            try:
                del record['data']
                deleted_count += 1
            except Exception as e:
                print(f"Failed to delete {record.get('id', 'unknown')}: {e}")
        
        if deleted_count > 0:
            print(f"Bulk deletion complete. Removed {deleted_count} records.")
        return deleted_count

    def reset(self):
        self.confirm_flag = False
