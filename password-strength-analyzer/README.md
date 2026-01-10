# Password Security Analyzer

This project analyzes password security using two fundamentally different approaches:

1. A rule-based security audit following classical password security principles.
2. A Machine Learning model trained on labeled password data.

The purpose of the project is to compare deterministic security rules with a data-driven approach.



## Rule-Based Password Audit

The rule-based script evaluates a password using multiple security checks:

- Comparison against a list of common passwords
- Minimum length validation
- Detection of character sets:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Special characters
- Estimation of password entropy in bits
- Classification based on entropy thresholds

The password is classified as:
- Insecure (common password or too short)
- Weak
- Acceptable
- Strong

This approach is deterministic, transparent, and follows classical cybersecurity practices.

## Machine Learning Approach

The ML-based solution uses a labeled dataset of passwords classified as strong or weak.

The process includes:

- Feature extraction from passwords
- Training a classification model
- Predicting password strength based on learned patterns

This approach allows the system to detect non-obvious patterns that rule-based systems may miss.

## Purpose

This project was created for educational and portfolio purposes, focusing on Python, cybersecurity fundamentals, and applied Machine Learning.

## Disclaimer

This project is intended for learning and demonstration only. It should not be used as a standalone security solution in production environments.

