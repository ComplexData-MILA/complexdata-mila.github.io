import unittest
import json
import os
import shutil
from pathlib import Path
from ruamel.yaml import YAML

import src.python.add_update_member as mod


class TestAddUpdateMember(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        yaml = YAML()
        yaml.preserve_quotes = True
        with open("_data/authors.yml") as f:
            cls.authors = yaml.load(f)

        cls.image_dir = "tests/scratch/assets/images/bio/"
        
        cls.site_data_dir = Path("tests/scratch/_data/")
        cls.site_data_dir.mkdir(parents=True, exist_ok=True)

        shutil.copy("_data/authors.yml", cls.site_data_dir / "authors.yml")


    
    @classmethod
    def tearDownClass(cls) -> None:
        for path in [
            cls.image_dir,
            cls.site_data_dir
        ]:
            if os.path.exists(path):
                shutil.rmtree(path)

    def test_add_member(self):
        self.maxDiff = None        
        with open("tests/data/add_member/in.md") as f:
            issue_body = f.read()

        parsed = mod.parse_issue_body(issue_body)
        out = mod.main(parsed, action="Add member", image_dir=self.image_dir, site_data_dir=self.site_data_dir)
        
        with open("tests/data/add_member/out.json") as f:
            expected = json.load(f)
        
        output = json.loads(json.dumps(out['John Doe']))

        self.assertEqual(output, expected)

    def test_update_member(self):
        self.maxDiff = None
        with open("tests/data/update_member/in.md") as f:
            issue_body = f.read()

        exp_out_path = "tests/data/update_member/out.json"
        parsed = mod.parse_issue_body(issue_body)
        out = mod.main(parsed, action="Update member", image_dir=self.image_dir, site_data_dir=self.site_data_dir)
        

        with open(exp_out_path) as f:
            expected = json.load(f)
        
        
        output = json.loads(json.dumps(out['John Doe']))

        # Sort output and expected dicts to make sure they are the same
        output = {k: output[k] for k in sorted(output)}
        expected = {k: expected[k] for k in sorted(expected)}

        error_message = f"\n\n!!! Expected content of generated file to match content of file {exp_out_path}, but they did not match !!!"
        
        self.assertEqual(output, expected, error_message)

        
    