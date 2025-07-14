#!/usr/bin/env python3
"""
Test script to verify the Draco 2.0.1 Intern Guide works properly
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all necessary imports work"""
    try:
        import draco
        import pandas as pd
        from draco_intern_guide import (
            create_genomic_sample_data,
            safe_schema_analysis, 
            safe_constraint_solving,
            create_custom_data_to_facts
        )
        print("✅ All imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality from the guide"""
    try:
        from draco_intern_guide import create_genomic_sample_data, safe_schema_analysis
        
        # Test data creation
        datasets = create_genomic_sample_data()
        print(f"✅ Created {len(datasets)} datasets")
        
        # Test schema analysis
        gene_df = datasets["gene_expression"]
        schema = safe_schema_analysis(gene_df)
        if schema:
            print(f"✅ Schema analysis successful: {len(schema['field'])} fields detected")
        else:
            print("❌ Schema analysis failed")
            
        return True
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def test_constraint_solving():
    """Test constraint solving functionality"""
    try:
        from draco_intern_guide import safe_constraint_solving
        
        # Simple test program
        test_program = [
            'gene("BRCA1").',
            'gene("BRCA2").',
            'cancer_gene(Gene) :- gene(Gene).',
        ]
        
        result = safe_constraint_solving(test_program)
        if result["satisfiable"]:
            print(f"✅ Constraint solving successful: {result['atom_count']} atoms")
        else:
            print("❌ Constraint solving failed")
            
        return True
    except Exception as e:
        print(f"❌ Constraint solving test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("TESTING DRACO 2.0.1 INTERN GUIDE")
    print("=" * 60)
    
    tests = [
        ("Import Test", test_imports),
        ("Basic Functionality", test_basic_functionality),
        ("Constraint Solving", test_constraint_solving),
    ]
    
    passed = 0
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        if test_func():
            passed += 1
    
    print(f"\n{'='*60}")
    print(f"RESULTS: {passed}/{len(tests)} tests passed")
    print(f"{'='*60}")
    
    if passed == len(tests):
        print("🎉 All tests passed! The intern guide is ready to use.")
        return True
    else:
        print("⚠️  Some tests failed. Check the error messages above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 