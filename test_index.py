import unittest
import os
from html.parser import HTMLParser


class HTMLDOMParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.current_tag = None
        self.meta_tags = []
        self.h1_texts = []
        self.p_texts = []
        self.in_h1 = False
        self.in_p = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.tags.append((tag, attrs_dict))
        if tag == "meta":
            self.meta_tags.append(attrs_dict)
        elif tag == "h1":
            self.in_h1 = True
            self.current_h1 = []
        elif tag == "p":
            self.in_p = True
            self.current_p = []

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_h1 = False
            self.h1_texts.append("".join(self.current_h1).strip())
        elif tag == "p":
            self.in_p = False
            self.p_texts.append("".join(self.current_p).strip())

    def handle_data(self, data):
        if self.in_h1:
            self.current_h1.append(data)
        if self.in_p:
            self.current_p.append(data)


class TestLandingPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base_dir = os.path.dirname(__file__)
        cls.html_path = os.path.join(base_dir, "index.html")
        cls.css_path = os.path.join(base_dir, "styles.css")
        with open(cls.html_path, "r", encoding="utf-8") as f:
            cls.html_content = f.read()
        with open(cls.css_path, "r", encoding="utf-8") as f:
            cls.css_content = f.read()

        cls.parser = HTMLDOMParser()
        cls.parser.feed(cls.html_content)

    def test_doctype_and_html5_structure(self):
        self.assertTrue(self.html_content.strip().startswith("<!DOCTYPE html>"))
        tag_names = [t[0] for t in self.parser.tags]
        self.assertIn("html", tag_names)
        self.assertIn("head", tag_names)
        self.assertIn("body", tag_names)
        self.assertIn("main", tag_names)
        self.assertIn("section", tag_names)

    def test_meta_charset_and_viewport(self):
        has_charset = any("charset" in attrs and attrs["charset"].lower() == "utf-8" for attrs in self.parser.meta_tags)
        self.assertTrue(has_charset, "Missing meta charset UTF-8")

        viewport_meta = next((attrs for attrs in self.parser.meta_tags if attrs.get("name") == "viewport"), None)
        self.assertIsNotNone(viewport_meta, "Missing meta viewport tag")
        self.assertIn("width=device-width", viewport_meta.get("content", ""))
        self.assertIn("initial-scale=1.0", viewport_meta.get("content", ""))

    def test_h1_exact_text(self):
        self.assertIn("Artisan Demo", self.parser.h1_texts, "h1 must contain exact text 'Artisan Demo'")

    def test_tagline_paragraph(self):
        tagline_match = any(
            "autonomous multi-agent" in text.lower() and "github" in text.lower() and "jira" in text.lower()
            for text in self.parser.p_texts
        )
        self.assertTrue(tagline_match, "Paragraph should contain tagline describing autonomous multi-agent GitHub/Jira automation")

    def test_hero_css_styling(self):
        self.assertIn(".hero", self.css_content)
        self.assertIn("text-align: center", self.css_content)
        self.assertIn("align-items: center", self.css_content)
        self.assertIn("@media", self.css_content)

    def test_accessibility_elements(self):
        html_tags = [attrs for tag, attrs in self.parser.tags if tag == "html"]
        self.assertTrue(any(attrs.get("lang") == "en" for attrs in html_tags), "html tag missing lang attribute")


if __name__ == "__main__":
    unittest.main()
