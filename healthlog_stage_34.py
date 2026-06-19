# === Stage 34: Add support for multiple local user profiles ===
# Project: HealthLog
import json, os
from pathlib import Path

class UserProfiles:
    def __init__(self, data_dir="healthlog_data"):
        self.data_dir = Path(data_dir)
        self.profiles_file = self.data_dir / "profiles.json"
        if not self.data_dir.exists():
            self.data_dir.mkdir()
    
    def load_profiles(self):
        try:
            with open(self.profiles_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_profiles(self, profiles):
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.profiles_file, 'w', encoding='utf-8') as f:
            json.dump(profiles, f, ensure_ascii=False, indent=2)
    
    def add_profile(self, name, email=None, theme="light"):
        profiles = self.load_profiles()
        if any(p['name'] == name for p in profiles):
            raise ValueError(f"Profile {name} already exists")
        profile = {"id": len(profiles)+1, "name": name, "email": email or "", "theme": theme}
        profiles.append(profile)
        self.save_profiles(profiles)
        return profile
    
    def get_profile(self, name):
        for p in self.load_profiles():
            if p['name'] == name:
                return p
        return None

profiles = UserProfiles()
