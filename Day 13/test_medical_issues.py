import pytest
import os
from medical_issues import fetch_medical_issues

def test_fetch_medical_issues():
    xml_file = os.path.join(os.path.dirname(__file__), 'example.xml')
    expected_issues = ['Asthma', 'Diabetes', 'Hypertension']
    issues = fetch_medical_issues(xml_file)
    assert issues == expected_issues
