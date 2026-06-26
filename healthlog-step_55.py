# === Stage 55: Add a setting to disable colorized output ===
# Project: HealthLog
class ColorSettings:
    def __init__(self, enable_color=True):
        self.enable_color = enable_color
    
    @staticmethod
    def is_enabled():
        return os.environ.get('NO_COLOR', '').lower() in ('1', 'true') or not sys.stdout.isatty()
    
    def get_output(self, text: str) -> str:
        if not self.enable_color and not ColorSettings.is_enabled():
            return text
        return text

def setup_logging_config(enable_colors=True):
    from rich.console import Console
    
    console = Console(
        force_terminal=sys.stdout.isatty(),
        color_system='auto' if enable_colors else None,
        highlight=False,
        style=None,
        no_color=not enable_colors and not sys.stdout.isatty()
    )
    
    def log_info(msg):
        print(f"[dim]ℹ {msg}[/]", file=sys.stderr)
        
    def log_error(msg):
        print(f"[red]✖ {msg}[/]", file=sys.stderr)
        
    return console, log_info, log_error

def get_weekly_summary_data():
    from datetime import datetime, timedelta
    
    today = datetime.now()
    week_start = (today - timedelta(days=today.weekday())).date()
    
    data = {
        'week_start': week_start.isoformat(),
        'days_logged': 0,
        'habits_completed': [],
        'measurements_avg': {},
        'symptoms_count': {}
    }
    
    # Simulated data retrieval logic would go here
    return data

def generate_summary_report(data):
    from rich.table import Table
    
    table = Table(title="Weekly Wellness Summary")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", justify="right")
    
    if 'days_logged' in data:
        table.add_row(f"Days Logged ({data['week_start']} - {today.date().isoformat()})", str(data.get('days_logged', 0)))
        
    return table

def main():
    import sys
    
    try:
        from rich.console import Console
        console = Console(force_terminal=sys.stdout.isatty())
        
        # Example usage with color disabled via environment variable
        if 'NO_COLOR' in os.environ:
            print("Color output disabled by NO_COLOR flag")
            
        # Generate and display summary
        data = get_weekly_summary_data()
        report_table = generate_summary_report(data)
        console.print(report_table)
        
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")

if __name__ == "__main__":
    main()
