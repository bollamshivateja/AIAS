import unittest
from Task1 import is_valid_email


class TestEmailValidation(unittest.TestCase):
    
    def test_valid_emails(self):
        valid_emails = [
            "user@domain.com",
            "test.email@example.org",
            "user123@domain123.co.uk",
            "a@b.c",
            "user_name@domain-name.com",
            "user-name@domain_name.org",
            "user123@domain456.net",
            "test@sub.domain.com",
            "user@domain.co.in",
            "admin@company.org"
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))
    
    def test_invalid_no_at_symbol(self):
        invalid_emails = [
            "userdomain.com",
            "test.email.example.org",
            "user123domain123.co.uk",
            "plainaddress"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
    
    def test_invalid_multiple_at_symbols(self):
        invalid_emails = [
            "user@@domain.com",
            "user@domain@com",
            "user@domain@com@extra",
            "test@@example.org",
            "user@domain@sub@com"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
    
    def test_invalid_no_dot(self):
        invalid_emails = [
            "user@domain",
            "test@example",
            "user123@domain123",
            "admin@company",
            "user@localhost"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
    
    def test_invalid_starts_with_at(self):
        invalid_emails = [
            "@domain.com",
            "@example.org",
            "@user.domain.com",
            "@test.co.uk"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
    
    def test_invalid_ends_with_at(self):
        invalid_emails = [
            "user@",
            "test@",
            "user123@",
            "admin@"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
    
    def test_invalid_starts_with_dot(self):
        invalid_emails = [
            ".user@domain.com",
            ".test@example.org",
            ".user123@domain.co.uk"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
    
    def test_invalid_ends_with_dot(self):
        invalid_emails = [
            "user@domain.com.",
            "test@example.org.",
            "user123@domain.co.uk."
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
    
    def test_invalid_special_characters(self):
        invalid_emails = [
            "user@domain.com!",
            "test@example.org#",
            "user@domain.com$",
            "test@example.org%",
            "user@domain.com^",
            "test@example.org&",
            "user@domain.com*",
            "test@example.org(",
            "user@domain.com)",
            "test@example.org+",
            "user@domain.com=",
            "test@example.org[",
            "user@domain.com]",
            "test@example.org{",
            "user@domain.com}",
            "user@domain.com|",
            "test@example.org\\",
            "user@domain.com/",
            "test@example.org?",
            "user@domain.com<",
            "test@example.org>",
            "user@domain.com,",
            "test@example.org;",
            "user@domain.com:",
            "test@example.org\"",
            "user@domain.com'",
            "test@example.org`",
            "user@domain.com~"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
    
    def test_invalid_spaces(self):
        invalid_emails = [
            "user @domain.com",
            "test@ example.org",
            "user @ domain.com",
            " test@domain.com",
            "test@domain.com ",
            " test@domain.com "
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
    
    def test_edge_cases(self):
        edge_cases = [
            ("", False),
            ("a@b.c", True),
            ("a@b.c.d", True),
            ("user@domain.co.uk", True),
            ("user@sub.domain.com", True),
            ("user@domain-name.com", True),
            ("user_name@domain.com", True),
            ("user-name@domain.com", True),
            ("user123@domain456.com", True)
        ]
        
        for email, expected in edge_cases:
            with self.subTest(email=email):
                self.assertEqual(is_valid_email(email), expected)
    
    def test_case_sensitivity(self):
        valid_emails = [
            "User@Domain.com",
            "TEST@EXAMPLE.ORG",
            "User123@Domain456.NET",
            "Test.Email@Example.Org"
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))


if __name__ == "__main__":
    unittest.main()
