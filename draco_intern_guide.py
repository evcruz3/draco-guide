"""
Draco 2.0.1 Intern Guide - Comprehensive Method Coverage
=======================================================

This guide demonstrates the working methods in Draco 2.0.1 based on comprehensive testing.
We focus on practical applications using genomic dataset examples.

✅ Available Methods:
- schema_from_dataframe() - data analysis
- schema_from_file() - file-based data analysis
- dict_to_facts() - dictionary to ASP facts conversion
- is_satisfiable() - constraint testing
- run_clingo() - ASP solving
- answer_set_to_dict() - ASP processing
- complete_spec() - specification completion
- Draco class properties - constraint exploration

Author: Generated from comprehensive Draco 2.0.1 testing
"""

import draco
import pandas as pd
import json
from typing import Dict, List, Any, Optional, Union

# ==========================================
# SECTION 1: BASIC SETUP AND INSTALLATION
# ==========================================

def setup_info():
    """
    Display setup information for Draco 2.0.1
    """
    print("=== Draco 2.0.1 Setup Information ===")
    print("Installation: pip install draco")
    print("Current version: 2.0.1")
    print("Dependencies: clingo (auto-installed)")
    print("Python compatibility: 3.8+")
    print()

# ==========================================
# SECTION 2: GENOMIC DATA EXAMPLES
# ==========================================

def create_genomic_sample_data():
    """
    Create sample genomic datasets for demonstration
    """
    print("=== Creating Sample Genomic Datasets ===")
    
    # Gene expression data
    gene_expression_data = [
        {"gene_id": "BRCA1", "expression_level": 45.2, "tissue": "breast", "sample_id": "S001"},
        {"gene_id": "BRCA2", "expression_level": 32.8, "tissue": "breast", "sample_id": "S001"},
        {"gene_id": "TP53", "expression_level": 67.1, "tissue": "breast", "sample_id": "S001"},
        {"gene_id": "BRCA1", "expression_level": 12.3, "tissue": "liver", "sample_id": "S002"},
        {"gene_id": "BRCA2", "expression_level": 23.7, "tissue": "liver", "sample_id": "S002"},
        {"gene_id": "TP53", "expression_level": 89.4, "tissue": "liver", "sample_id": "S002"},
        {"gene_id": "EGFR", "expression_level": 156.8, "tissue": "lung", "sample_id": "S003"},
        {"gene_id": "KRAS", "expression_level": 78.9, "tissue": "lung", "sample_id": "S003"},
    ]
    
    # Variant data
    variant_data = [
        {"chromosome": "chr1", "position": 43094077, "ref_allele": "G", "alt_allele": "A", "quality": 99.9},
        {"chromosome": "chr1", "position": 43094078, "ref_allele": "C", "alt_allele": "T", "quality": 95.2},
        {"chromosome": "chr2", "position": 25457242, "ref_allele": "T", "alt_allele": "G", "quality": 87.3},
        {"chromosome": "chr2", "position": 25457243, "ref_allele": "A", "alt_allele": "C", "quality": 92.1},
        {"chromosome": "chr3", "position": 12393847, "ref_allele": "G", "alt_allele": "T", "quality": 98.7},
    ]
    
    # Clinical data
    clinical_data = [
        {"patient_id": "P001", "age": 45, "gender": "female", "diagnosis": "breast_cancer", "stage": "II"},
        {"patient_id": "P002", "age": 62, "gender": "male", "diagnosis": "lung_cancer", "stage": "III"},
        {"patient_id": "P003", "age": 38, "gender": "female", "diagnosis": "breast_cancer", "stage": "I"},
        {"patient_id": "P004", "age": 71, "gender": "male", "diagnosis": "liver_cancer", "stage": "IV"},
        {"patient_id": "P005", "age": 29, "gender": "female", "diagnosis": "breast_cancer", "stage": "II"},
    ]
    
    return {
        "gene_expression": pd.DataFrame(gene_expression_data),
        "variants": pd.DataFrame(variant_data),
        "clinical": pd.DataFrame(clinical_data)
    }

# ==========================================
# SECTION 3: SCHEMA ANALYSIS (✅ WORKS)
# ==========================================

def demonstrate_schema_analysis():
    """
    Demonstrate schema_from_dataframe() - reliable data analysis feature
    """
    print("=== METHOD 1: Schema Analysis (schema_from_dataframe) ===")
    print("✅ Status: WORKS PERFECTLY")
    print("📝 Description: Analyzes data structure and provides field statistics")
    print()
    
    datasets = create_genomic_sample_data()
    
    for dataset_name, df in datasets.items():
        print(f"--- Analyzing {dataset_name.upper()} Dataset ---")
        print(f"Data shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print()
        
        try:
            # This is the main working method in Draco 2.0.1
            schema = draco.schema_from_dataframe(df)
            
            print("Schema Analysis Results:")
            print(f"Number of fields: {len(schema['field'])}")
            
            for field in schema['field']:
                print(f"  📊 Field: {field['name']}")
                print(f"     Type: {field['type']}")
                
                # Show statistics if available
                if 'stats' in field:
                    stats = field['stats']
                    if field['type'] == 'quantitative':
                        print(f"     Min: {stats.get('min', 'N/A')}")
                        print(f"     Max: {stats.get('max', 'N/A')}")
                        print(f"     Mean: {stats.get('mean', 'N/A')}")
                        print(f"     Std: {stats.get('std', 'N/A')}")
                    elif field['type'] == 'nominal':
                        print(f"     Unique values: {stats.get('unique', 'N/A')}")
                        print(f"     Entropy: {stats.get('entropy', 'N/A')}")
                
                print()
            
            # Show practical applications
            print("🔧 Practical Applications:")
            print("- Automatic data type detection")
            print("- Statistical summary generation")
            print("- Data quality assessment")
            print("- Visualization recommendation input")
            print()
            
        except Exception as e:
            print(f"❌ Error in schema analysis: {e}")
            print()

# ==========================================
# SECTION 4: FILE-BASED SCHEMA ANALYSIS
# ==========================================

def demonstrate_file_schema_analysis():
    """
    Demonstrate schema_from_file() with Path objects
    """
    print("=== METHOD 2: File-Based Schema Analysis (schema_from_file) ===")
    print("✅ Status: WORKS WITH PATH OBJECTS")
    print("📝 Description: Loads and analyzes data from files (CSV/JSON)")
    print()
    
    # Create sample data files
    import tempfile
    import os
    from pathlib import Path
    
    # Create temporary directory
    temp_dir = tempfile.mkdtemp()
    
    # Create sample CSV
    sample_data = create_genomic_sample_data()["gene_expression"]
    csv_path = os.path.join(temp_dir, "gene_expression.csv")
    sample_data.to_csv(csv_path, index=False)
    
    # Create sample JSON
    json_path = os.path.join(temp_dir, "gene_expression.json")
    sample_data.to_json(json_path, orient="records")
    
    # Method 1: CSV file with Path object
    print("Method 1: CSV file with Path object")
    try:
        schema = draco.schema_from_file(Path(csv_path))
        print(f"✅ CSV file worked: {len(schema['field'])} fields analyzed")
        for field in schema['field']:
            print(f"  - {field['name']}: {field['type']}")
        print()
    except Exception as e:
        print(f"❌ CSV file failed: {e}")
    
    # Method 2: JSON file with Path object
    print("Method 2: JSON file with Path object")
    try:
        schema = draco.schema_from_file(Path(json_path))
        print(f"✅ JSON file worked: {len(schema['field'])} fields analyzed")
        for field in schema['field']:
            print(f"  - {field['name']}: {field['type']}")
        print()
    except Exception as e:
        print(f"❌ JSON file failed: {e}")
    
    # Cleanup
    import shutil
    shutil.rmtree(temp_dir)
    
    print("🔑 Key Insights:")
    print("- Always wrap file paths in Path() objects")
    print("- Works with both CSV and JSON files")
    print("- Identical results to pandas + schema_from_dataframe")
    print("- Perfect for file-based genomic data analysis")
    print()

# ==========================================
# SECTION 5: DICTIONARY TO FACTS CONVERSION
# ==========================================

def demonstrate_dict_to_facts():
    """
    Demonstrate dict_to_facts() with correct usage patterns
    """
    print("=== METHOD 3: Dictionary to Facts Conversion (dict_to_facts) ===")
    print("✅ Status: WORKS WITH CORRECT PARAMETERS")
    print("📝 Description: Converts dictionaries to ASP facts")
    print()
    
    # Method 1: Simple dictionary
    print("Method 1: Simple dictionary")
    simple_dict = {"name": "BRCA1", "expression": 45.2}
    try:
        facts = draco.dict_to_facts(simple_dict)
        print(f"✅ Simple dict worked: {len(facts)} facts")
        for fact in facts:
            print(f"  {fact}")
        print()
    except Exception as e:
        print(f"❌ Simple dict failed: {e}")
    
    # Method 2: Nested dictionary
    print("Method 2: Nested dictionary")
    nested_dict = {
        "gene_data": {
            "BRCA1": {"expression": 45.2, "tissue": "breast"},
            "BRCA2": {"expression": 32.8, "tissue": "breast"}
        }
    }
    try:
        facts = draco.dict_to_facts(nested_dict)
        print(f"✅ Nested dict worked: {len(facts)} facts")
        for fact in facts[:5]:
            print(f"  {fact}")
        if len(facts) > 5:
            print(f"  ... and {len(facts) - 5} more")
        print()
    except Exception as e:
        print(f"❌ Nested dict failed: {e}")
    
    # Method 3: Dictionary with custom path
    print("Method 3: Dictionary with custom path")
    data = {"gene": "BRCA1", "value": 45}
    try:
        facts = draco.dict_to_facts(data, path=("root",))
        print(f"✅ Custom path worked: {len(facts)} facts")
        for fact in facts:
            print(f"  {fact}")
        print()
    except Exception as e:
        print(f"❌ Custom path failed: {e}")
    
    print("🔑 Key Insights:")
    print("- Use dictionaries, not lists")
    print("- Nested dictionaries work well")
    print("- Custom path parameter prevents index errors")
    print("- Perfect for structured genomic data")
    print()

# ==========================================
# SECTION 6: CONSTRAINT SOLVING (✅ WORKS)  
# ==========================================

def demonstrate_constraint_solving():
    """
    Demonstrate is_satisfiable() and run_clingo() - ASP constraint solving
    """
    print("=== METHOD 4: Constraint Solving (is_satisfiable & run_clingo) ===")
    print("✅ Status: WORKS WELL")
    print("📝 Description: Solves Answer Set Programming (ASP) constraint problems")
    print()
    
    # Example 1: Basic genomic constraint
    print("--- Example 1: Basic Genomic Data Constraint ---")
    genomic_program = [
        'data("BRCA1", gene_id, 0).',
        'data(45, expression_level, 0).',
        'data("breast", tissue, 0).',
        'fieldtype(gene_id, nominal).',
        'fieldtype(expression_level, quantitative).',
        'fieldtype(tissue, nominal).',
        'high_expression(Gene) :- data(Gene, gene_id, Row), data(Level, expression_level, Row), Level > 40.',
    ]
    
    try:
        # Check if the program is satisfiable
        is_sat = draco.is_satisfiable(genomic_program)
        print(f"Program is satisfiable: {is_sat}")
        
        if is_sat:
            # Generate models (solutions)
            models = list(draco.run_clingo(genomic_program, models=2))
            print(f"Generated {len(models)} model(s)")
            
            # Examine first model
            if models:
                model = models[0]
                answer_set = list(model.answer_set)
                print(f"First model has {len(answer_set)} atoms")
                
                # Show some atoms
                print("Sample atoms from the model:")
                for i, atom in enumerate(answer_set):
                    if i < 5:  # Show first 5 atoms
                        print(f"  {atom}")
                    else:
                        break
                        
        print()
        
    except Exception as e:
        print(f"❌ Error in constraint solving: {e}")
        print()
    
    # Example 2: Variant quality constraint
    print("--- Example 2: Variant Quality Constraint ---")
    variant_program = [
        'variant("chr1", 43094077, "G", "A", 99).',
        'variant("chr1", 43094078, "C", "T", 95).',
        'variant("chr2", 25457242, "T", "G", 87).',
        'high_quality(Chr, Pos) :- variant(Chr, Pos, _, _, Quality), Quality > 90.',
        'low_quality(Chr, Pos) :- variant(Chr, Pos, _, _, Quality), Quality <= 90.',
    ]
    
    try:
        is_sat = draco.is_satisfiable(variant_program)
        print(f"Variant program is satisfiable: {is_sat}")
        
        if is_sat:
            models = list(draco.run_clingo(variant_program, models=1))
            print(f"Generated {len(models)} model(s)")
            
            if models:
                model = models[0]
                answer_set = list(model.answer_set)
                print("Variant analysis results:")
                for atom in answer_set:
                    atom_str = str(atom)
                    if 'high_quality' in atom_str or 'low_quality' in atom_str:
                        print(f"  {atom_str}")
        
        print()
        
    except Exception as e:
        print(f"❌ Error in variant constraint solving: {e}")
        print()

# ==========================================
# SECTION 7: SPECIFICATION COMPLETION
# ==========================================

def demonstrate_spec_completion():
    """
    Demonstrate complete_spec() with proper Vega-Lite specifications
    """
    print("=== METHOD 5: Specification Completion (complete_spec) ===")
    print("✅ Status: WORKS WITH PROPER VEGA-LITE SPECS")
    print("📝 Description: Completes partial Vega-Lite specifications")
    print()
    
    # Method 1: Simple specification
    print("Method 1: Simple specification")
    simple_spec = {
        "data": {"url": "gene_data.csv"},
        "mark": "point",
        "encoding": {
            "x": {"field": "gene_id", "type": "nominal"},
            "y": {"field": "expression_level", "type": "quantitative"}
        }
    }
    
    try:
        d = draco.Draco()
        result = d.complete_spec(simple_spec, models=1)
        print(f"✅ Simple spec worked: {type(result)}")
        print("Generated specification completion")
        print()
    except Exception as e:
        print(f"❌ Simple spec failed: {e}")
    
    # Method 2: Minimal specification
    print("Method 2: Minimal specification")
    minimal_spec = {
        "mark": "point"
    }
    
    try:
        d = draco.Draco()
        result = d.complete_spec(minimal_spec, models=1)
        print(f"✅ Minimal spec worked: {type(result)}")
        print("Generated completion for minimal spec")
        print()
    except Exception as e:
        print(f"❌ Minimal spec failed: {e}")
    
    print("🔑 Key Insights:")
    print("- Use proper Vega-Lite specification format")
    print("- Minimal specifications work too")
    print("- Great for automated chart generation")
    print()

# ==========================================
# SECTION 8: ASP RESULT PROCESSING
# ==========================================

def demonstrate_asp_processing():
    """
    Demonstrate answer_set_to_dict() - ASP result processing
    """
    print("=== METHOD 6: ASP Result Processing (answer_set_to_dict) ===")
    print("⚠️  Status: WORKS BUT LIMITED")
    print("📝 Description: Converts ASP answer sets to dictionaries")
    print()
    
    # Simple program for testing
    test_program = [
        'gene("BRCA1").',
        'gene("BRCA2").',
        'cancer_related(Gene) :- gene(Gene).',
        'important(Gene) :- cancer_related(Gene).',
    ]
    
    try:
        # Generate models
        models = list(draco.run_clingo(test_program, models=1))
        
        if models:
            model = models[0]
            answer_set = list(model.answer_set)
            print(f"Model has {len(answer_set)} atoms")
            
            # Try to convert to dictionary
            result_dict = draco.answer_set_to_dict(model.answer_set)
            print(f"Dictionary conversion result: {result_dict}")
            
            # Manual processing is more reliable
            print("\nManual processing of answer set:")
            atoms_by_predicate = {}
            for atom in answer_set:
                atom_str = str(atom)
                predicate = atom_str.split('(')[0] if '(' in atom_str else atom_str
                if predicate not in atoms_by_predicate:
                    atoms_by_predicate[predicate] = []
                atoms_by_predicate[predicate].append(atom_str)
            
            for predicate, atoms in atoms_by_predicate.items():
                print(f"  {predicate}: {atoms}")
                
        print()
        
    except Exception as e:
        print(f"❌ Error in ASP processing: {e}")
        print()

# ==========================================
# SECTION 9: DRACO CLASS PROPERTIES
# ==========================================

def demonstrate_draco_properties():
    """
    Demonstrate Draco class properties - constraint system access
    """
    print("=== METHOD 7: Draco Class Properties (constraints, helpers, etc.) ===")
    print("✅ Status: WORKS WELL")
    print("📝 Description: Access to ASP constraints and helper definitions")
    print()
    
    try:
        # Create Draco instance
        d = draco.Draco()
        
        # Show available properties
        print("Available Draco properties:")
        properties = ['constraints', 'helpers', 'soft_constraint_names', 'weights']
        for prop in properties:
            if hasattr(d, prop):
                print(f"  ✅ {prop}")
            else:
                print(f"  ❌ {prop}")
        
        print()
        
        # Examine soft constraint names
        if hasattr(d, 'soft_constraint_names'):
            constraint_names = d.soft_constraint_names
            print(f"Total soft constraints: {len(constraint_names)}")
            print("Sample constraint names:")
            for i, name in enumerate(constraint_names[:10]):
                print(f"  {i+1}. {name}")
            if len(constraint_names) > 10:
                print(f"  ... and {len(constraint_names) - 10} more")
        
        print()
        
        # Show sample constraints
        if hasattr(d, 'constraints'):
            constraints = d.constraints
            print("Sample constraint definitions:")
            constraint_lines = constraints.split('\n')[:5]
            for i, line in enumerate(constraint_lines):
                if line.strip():
                    print(f"  {i+1}. {line}")
        
        print()
        
        # Show sample helpers
        if hasattr(d, 'helpers'):
            helpers = d.helpers
            print("Sample helper definitions:")
            helper_lines = helpers.split('\n')[:5]
            for i, line in enumerate(helper_lines):
                if line.strip():
                    print(f"  {i+1}. {line}")
        
        print()
        
    except Exception as e:
        print(f"❌ Error accessing Draco properties: {e}")
        print()

# ==========================================
# SECTION 10: PRACTICAL UTILITIES
# ==========================================

def create_custom_data_to_facts(data: List[Dict]) -> List[str]:
    """
    Custom replacement for enhanced data-to-facts conversion
    """
    facts = []
    for row_idx, row in enumerate(data):
        for field, value in row.items():
            if isinstance(value, str):
                facts.append(f'data("{value}", {field}, {row_idx}).')
            elif isinstance(value, float):
                # Convert float to int for ASP compatibility
                facts.append(f'data({int(value)}, {field}, {row_idx}).')
            else:
                facts.append(f'data({value}, {field}, {row_idx}).')
    return facts

def safe_dict_to_facts(data: Union[List[Dict], Dict]) -> List[str]:
    """
    Safe wrapper for dict_to_facts() that handles both lists and dictionaries
    """
    try:
        if isinstance(data, list):
            # Convert list to dictionary format that works with dict_to_facts
            data_dict = {"records": data}
            return draco.dict_to_facts(data_dict)
        else:
            # Use directly if it's already a dictionary
            return draco.dict_to_facts(data)
    except Exception as e:
        print(f"dict_to_facts failed: {e}")
        # Fallback to custom implementation
        if isinstance(data, list):
            return create_custom_data_to_facts(data)
        else:
            return []

def safe_schema_from_file(file_path: str) -> Union[Any, None]:
    """
    Safe wrapper for schema_from_file() that handles Path objects
    """
    try:
        from pathlib import Path
        return draco.schema_from_file(Path(file_path))
    except Exception as e:
        print(f"schema_from_file failed: {e}")
        # Fallback to pandas approach
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            elif file_path.endswith('.json'):
                df = pd.read_json(file_path)
            else:
                raise ValueError(f"Unsupported file type: {file_path}")
            return draco.schema_from_dataframe(df)
        except Exception as e2:
            print(f"Fallback failed: {e2}")
            return None

def safe_schema_analysis(df: pd.DataFrame) -> Union[Any, None]:
    """
    Safe wrapper for schema analysis with error handling
    """
    try:
        return draco.schema_from_dataframe(df)
    except Exception as e:
        print(f"Schema analysis failed: {e}")
        return None

def safe_constraint_solving(program: List[str]) -> Dict[str, Any]:
    """
    Safe wrapper for constraint solving with comprehensive error handling
    """
    result = {
        "satisfiable": False,
        "models": [],
        "errors": []
    }
    
    try:
        # Test satisfiability
        result["satisfiable"] = draco.is_satisfiable(program)
        
        if result["satisfiable"]:
            # Generate models
            models = list(draco.run_clingo(program, models=1))
            result["models"] = models
            
            # Process models
            if models:
                model = models[0]
                answer_set = list(model.answer_set)
                result["atom_count"] = len(answer_set)
                result["atoms"] = [str(atom) for atom in answer_set]
                
    except Exception as e:
        result["errors"].append(str(e))
    
    return result

# ==========================================
# SECTION 11: COMPLETE DEMONSTRATION
# ==========================================

def run_complete_demonstration():
    """
    Run the complete demonstration of working Draco 2.0.1 methods
    """
    print("=" * 80)
    print("DRACO 2.0.1 INTERN GUIDE - COMPLETE DEMONSTRATION")
    print("=" * 80)
    print()
    
    # Setup information
    setup_info()
    
    # Demonstrate each working method
    demonstrate_schema_analysis()
    print("=" * 50)
    demonstrate_file_schema_analysis()
    print("=" * 50)
    demonstrate_dict_to_facts()
    print("=" * 50)
    demonstrate_constraint_solving()
    print("=" * 50)
    demonstrate_spec_completion()
    print("=" * 50)
    demonstrate_asp_processing()
    print("=" * 50)
    demonstrate_draco_properties()
    print("=" * 50)
    
    # Practical example combining methods
    print("=== PRACTICAL EXAMPLE: Combining Methods ===")
    print("Scenario: Analyze gene expression data using multiple methods")
    print()
    
    # Create sample data
    datasets = create_genomic_sample_data()
    gene_df = datasets["gene_expression"]
    
    # Step 1: Schema analysis
    print("Step 1: Schema Analysis")
    schema = safe_schema_analysis(gene_df)
    if schema:
        print(f"✅ Analyzed {len(schema['field'])} fields")
        for field in schema['field']:
            print(f"  - {field['name']}: {field['type']}")
    
    print()
    
    # Step 2: Dictionary to facts conversion
    print("Step 2: Dictionary to Facts Conversion")
    gene_dict = {
        "gene_expression": {
            "BRCA1": {"expression": 45.2, "tissue": "breast"},
            "BRCA2": {"expression": 32.8, "tissue": "breast"},
            "TP53": {"expression": 67.1, "tissue": "breast"}
        }
    }
    
    try:
        dict_facts = draco.dict_to_facts(gene_dict)
        print(f"✅ Dict to facts worked: {len(dict_facts)} facts generated")
        for fact in dict_facts[:3]:
            print(f"  {fact}")
        if len(dict_facts) > 3:
            print(f"  ... and {len(dict_facts) - 3} more")
    except Exception as e:
        print(f"❌ Dict to facts failed: {e}")
    
    print()
    
    # Step 3: Custom data-to-facts conversion
    print("Step 3: Custom Data-to-Facts Conversion")
    sample_data = gene_df.head(3).to_dict('records')
    facts = create_custom_data_to_facts(sample_data)
    print(f"✅ Generated {len(facts)} ASP facts")
    for fact in facts[:5]:
        print(f"  {fact}")
    if len(facts) > 5:
        print(f"  ... and {len(facts) - 5} more")
    
    print()
    
    # Step 4: Constraint solving
    print("Step 4: Constraint Solving")
    extended_program = facts + [
        'fieldtype(gene_id, nominal).',
        'fieldtype(expression_level, quantitative).',
        'fieldtype(tissue, nominal).',
        'high_expression(Gene, Row) :- data(Gene, gene_id, Row), data(Level, expression_level, Row), Level > 40.',
        'tissue_gene(Tissue, Gene, Row) :- data(Tissue, tissue, Row), data(Gene, gene_id, Row).',
    ]
    
    result = safe_constraint_solving(extended_program)
    print(f"✅ Satisfiable: {result['satisfiable']}")
    if result['satisfiable'] and result['models']:
        print(f"✅ Generated {len(result['models'])} model(s)")
        print(f"✅ Found {result['atom_count']} atoms")
        
        # Show derived facts
        print("Derived facts:")
        for atom in result['atoms']:
            if 'high_expression' in atom or 'tissue_gene' in atom:
                print(f"  {atom}")
    
    print()
    
    # Step 5: Specification completion
    print("Step 5: Specification Completion")
    chart_spec = {
        "mark": "point",
        "encoding": {
            "x": {"field": "gene_id", "type": "nominal"},
            "y": {"field": "expression_level", "type": "quantitative"}
        }
    }
    
    try:
        d = draco.Draco()
        completed_spec = d.complete_spec(chart_spec, models=1)
        print(f"✅ Spec completion worked: {type(completed_spec)}")
        print("Generated chart specification completion")
    except Exception as e:
        print(f"❌ Spec completion failed: {e}")
    
    print()
    print("=" * 80)
    print("GUIDE COMPLETE - You now know all working methods in Draco 2.0.1!")
    print("=" * 80)

# ==========================================
# SECTION 12: BEST PRACTICES AND TIPS
# ==========================================

def print_best_practices():
    """
    Print best practices for working with Draco 2.0.1
    """
    print("=" * 80)
    print("DRACO 2.0.1 BEST PRACTICES FOR INTERNS")
    print("=" * 80)
    print()
    
    practices = [
        "✅ ALWAYS use schema_from_dataframe() for data analysis",
        "✅ USE pandas DataFrames as input for schema analysis",
        "✅ USE Path objects for schema_from_file()",
        "✅ USE dictionaries (not lists) for dict_to_facts()",
        "✅ USE proper Vega-Lite format for complete_spec()",
        "✅ IMPLEMENT error handling for all Draco function calls",
        "✅ TEST satisfiability before generating models",
        "✅ LIMIT model generation (models=1 or small numbers)",
        "✅ EXPLORE Draco class properties for advanced constraints",
        "✅ CREATE custom functions for enhanced reliability",
        "⚠️  USE answer_set_to_dict() cautiously - often returns empty results",
    ]
    
    for practice in practices:
        print(f"  {practice}")
    
    print()
    print("Remember: Draco 2.0.1 provides powerful constraint-based reasoning")
    print("when used with the correct parameter formats and error handling.")
    print()

# ==========================================
# MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    # Run the complete demonstration
    run_complete_demonstration()
    
    # Print best practices
    print_best_practices()
    
    # Additional resources
    print("=" * 80)
    print("ADDITIONAL RESOURCES")
    print("=" * 80)
    print("📚 Documentation: https://github.com/cmudig/draco")
    print("🐛 Bug Reports: Based on comprehensive testing - see DRACO_TESTING_RESULTS.md")
    print("🔧 Custom Solutions: Implement wrappers for enhanced functionality")
    print("📊 Alternative Tools: Consider Altair, Plotly, or ChartAdvisor for visualization")
    print("=" * 80) 