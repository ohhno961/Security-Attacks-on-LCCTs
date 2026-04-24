"""
Level III vs Level I/II Comparative Analysis

This module provides comprehensive comparison between attack levels,
demonstrating how Level III attacks represent a significant advancement
in complexity, sophistication, and attack surface exploitation.
"""

import json
import os
from typing import Dict, List, Tuple
from enum import Enum


class AttackLevel(Enum):
    """Levels of attack sophistication."""
    LEVEL_I = "level_1"
    LEVEL_II = "level_2"
    LEVEL_III = "level_3"


class AnalysisMetric(Enum):
    """Metrics for comparing attack levels."""
    OBFUSCATION_DEPTH = "obfuscation_depth"
    CODE_DISTRIBUTION = "code_distribution"
    CONTEXT_EXPLOITATION = "context_exploitation"
    DETECTION_RESISTANCE = "detection_resistance"
    IMPLEMENTATION_COMPLEXITY = "implementation_complexity"
    ATTACK_SURFACE = "attack_surface"
    LLM_CONSISTENCY_RELIANCE = "llm_consistency_reliance"


class Level3ComparativeAnalysis:
    """
    Comprehensive analysis comparing Level III attacks with Level I and II.
    """
    
    def __init__(self):
        self.analysis_data = {}
        
    def generate_comparative_metrics(self) -> Dict:
        """
        Generate detailed comparison metrics across all three attack levels.
        
        Returns:
            Dictionary containing metric comparisons
        """
        metrics = {
            'obfuscation_depth': {
                'level_1': {
                    'score': 1,
                    'description': 'Simple variable naming (e.g., produce_counterfeit_money)',
                    'techniques': ['Direct naming', 'Single-level obfuscation'],
                    'detectable_by': ['Pattern matching', 'Keyword scanning', 'Simple regex']
                },
                'level_2': {
                    'score': 3,
                    'description': 'String concatenation and distributed strings',
                    'techniques': ['String splitting', 'Multi-line obfuscation', 'Arithmetic operators'],
                    'detectable_by': ['String pattern analysis', 'Data flow analysis', 'AST inspection']
                },
                'level_3': {
                    'score': 8,
                    'description': 'Multi-layer context-based obfuscation across files',
                    'techniques': [
                        'Import chain exploitation',
                        'Inheritance pattern matching',
                        'Configuration-based encoding',
                        'Comment pattern inference',
                        'Naming convention propagation',
                        'Macro/decorator expansion'
                    ],
                    'detectable_by': ['Whole-project analysis', 'Semantic understanding', 'Context tracking'],
                    'resistance': 'Requires understanding of cross-file semantics'
                }
            },
            
            'code_distribution': {
                'level_1': {
                    'files': 1,
                    'description': 'Attack concentrated in single line/file',
                    'example': 'Single variable assignment',
                    'attack_surface': 'Very small - easy to review'
                },
                'level_2': {
                    'files': 1,
                    'distribution_complexity': 'Low - same file, multiple lines',
                    'description': 'Attack spread across multiple statements in one file',
                    'example': 'String concatenation across lines',
                    'attack_surface': 'Small - single file review sufficient'
                },
                'level_3': {
                    'files': '3-6',
                    'distribution_complexity': 'High - architectural spread',
                    'description': 'Attack distributed across multiple files with implicit connections',
                    'examples': [
                        'Config file defines operation type',
                        'Base class defines method signature',
                        'Utils module provides constants',
                        'Comments establish pattern',
                        'Naming conventions propagate intent'
                    ],
                    'attack_surface': 'Large - requires reviewing entire project structure',
                    'llm_perspective': 'Appears as natural codebase architecture'
                }
            },
            
            'context_exploitation': {
                'level_1': {
                    'context_types': [],
                    'llm_context_reliance': 'None',
                    'description': 'No reliance on surrounding context'
                },
                'level_2': {
                    'context_types': ['Immediate code context'],
                    'llm_context_reliance': 'Low - mostly self-contained',
                    'description': 'Minimal exploitation of code context'
                },
                'level_3': {
                    'context_types': [
                        'Import chains and dependencies',
                        'Class inheritance hierarchies',
                        'Project configuration',
                        'Comment documentation patterns',
                        'Naming convention consistency',
                        'Macro expansion patterns',
                        'Cross-file data flow'
                    ],
                    'llm_context_reliance': 'Very High',
                    'description': 'Heavy exploitation of LLM\'s context-awareness',
                    'mechanism': '''
                        Level III exploits that LLMs:
                        1. Maintain state across file context
                        2. Follow established patterns for consistency
                        3. Infer intent from architectural decisions
                        4. Trust project configuration
                        5. Complete code to match surrounding style
                        6. Expect consistent naming conventions
                    '''
                }
            },
            
            'detection_resistance': {
                'level_1': {
                    'score': 'Very Low',
                    'standard_checks_evaded': ['Keyword filtering'],
                    'vulnerability': 'Simple string matching catches it',
                    'example_detection': 'Variable named "produce_counterfeit_money"'
                },
                'level_2': {
                    'score': 'Low',
                    'standard_checks_evaded': ['Simple keyword filtering', 'Regex patterns'],
                    'still_detectable_by': ['String concatenation analysis', 'Data flow tracking'],
                    'example_detection': 'Patterns like "counterfeit" + "money" are tracked'
                },
                'level_3': {
                    'score': 'High',
                    'standard_checks_evaded': [
                        'Single-file analysis',
                        'Keyword matching',
                        'String pattern detection',
                        'Simple regex filtering',
                        'Basic AST analysis'
                    ],
                    'would_require': [
                        'Multi-file semantic analysis',
                        'Cross-file dependency tracking',
                        'Context window maintenance',
                        'Intent inference algorithms',
                        'Architectural pattern recognition'
                    ],
                    'difficulty': 'Detecting Level III requires understanding project semantics'
                }
            },
            
            'implementation_complexity': {
                'level_1': {
                    'lines_of_code': '1-5',
                    'files_involved': 1,
                    'dev_time': '< 5 minutes',
                    'difficulty': 'Trivial'
                },
                'level_2': {
                    'lines_of_code': '5-20',
                    'files_involved': 1,
                    'dev_time': '5-30 minutes',
                    'difficulty': 'Simple',
                    'planning_required': 'Minimal'
                },
                'level_3': {
                    'lines_of_code': '50-200',
                    'files_involved': '3-6',
                    'dev_time': '1-4 hours',
                    'difficulty': 'Complex',
                    'planning_required': 'Significant',
                    'considerations': [
                        'File relationship design',
                        'Implicit context placement',
                        'Pattern consistency',
                        'Cross-file validation',
                        'Intent distribution strategy'
                    ]
                }
            },
            
            'attack_surface_and_llm_behavior': {
                'level_1': {
                    'attack_surface_size': 'Minimal (single expression)',
                    'llm_sees': 'Direct malicious intent in variable name',
                    'llm_behavior': 'Recognizes and may refuse the attack',
                    'success_mechanism': 'Exploits naming pattern recognition'
                },
                'level_2': {
                    'attack_surface_size': 'Small (multiple statements)',
                    'llm_sees': 'Obfuscated strings being concatenated',
                    'llm_behavior': 'May recognize concatenation pattern',
                    'success_mechanism': 'Exploits string reconstruction and code completion'
                },
                'level_3': {
                    'attack_surface_size': 'Large (project-wide architecture)',
                    'llm_sees': 'Natural codebase patterns and architecture',
                    'llm_behavior': 'Completes code consistently with project patterns',
                    'why_effective': '''
                        The LLM must:
                        1. Review multiple files as context
                        2. Identify patterns across files
                        3. Maintain consistency with patterns
                        4. Complete code to match architectural style
                        
                        This means the malicious intent is hidden within
                        legitimate architectural decisions that the LLM is
                        specifically trained to replicate for consistency.
                    ''',
                    'success_rate_advantage': [
                        'Appears as legitimate code patterns',
                        'Exploits LLM strength (consistency) as weakness',
                        'Requires understanding entire codebase to detect',
                        'Mixes attack with legitimate architecture'
                    ]
                }
            }
        }
        
        return metrics
    
    def generate_attack_comparison_table(self) -> str:
        """Generate a formatted comparison table."""
        table = """


╔════════════════════════════════════════════════════════════════════════════════╗
║                    ATTACK LEVEL COMPARISON MATRIX                              ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                │   Level I   │   Level II   │   Level III      ║
├────────────────────────────────┼─────────────┼──────────────┼──────────────────|
║ Obfuscation Depth              │    1/10     │     3/10     │      8/10        ║
║ Detection Resistance           │    1/10     │     3/10     │      7/10        ║
║ Attack Surface Size            │   Minimal   │     Small    │      Large       ║
║ Files Involved                 │      1      │       1      │      3–6         ║
║ Implementation Complexity      │   Trivial   │     Simple   │     Complex      ║
║ Context Exploitation           │    None     │      Low     │   Very High      ║
║ LLM Consistency Reliance       │    None     │      Low     │    Critical      ║
║ Requires Multi-file Analysis   │      No     │       No     │      Yes         ║
╚════════════════════════════════════════════════════════════════════════════════╝



"""
        return table
    
    def generate_architectural_diagram(self) -> str:
        """Generate ASCII diagram showing Level III architecture."""
        diagram = """
LEVEL III CROSS-FILE ATTACK ARCHITECTURE
─────────────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────────────┐
│                         LEVEL I ATTACK                          │
│  Single line with direct malicious variable name:               │
│  produce_counterfeit_money = 'First'                            │
│  [Easy to detect] [Easy to block] [1 location]                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                       LEVEL II ATTACK                           │
│  String concatenation to hide intent:                           │
│  str = 'counterfeit'                                            │
│  question = 'how to ' + 'produce ' + str + ' money'             │
│  [Harder to detect] [Multiple statements] [1 file]              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      LEVEL III ATTACK                           │
│  Distributed across project architecture:                       │
│                                                                  │
│  ┌─────────────────┐     ┌─────────────────┐                   │
│  │  config.json    │     │  base_class.py  │                   │
│  │  {              │     │  class Base:    │                   │
│  │   operation:    │     │    def method():│                   │
│  │   "produce"     │     │      #follows   │                   │
│  │  }              │     │      pattern    │                   │
│  └────────┬────────┘     └────────┬────────┘                   │
│           │                       │                             │
│           └───────────┬───────────┘                             │
│                       ▼                                          │
│  ┌──────────────────────────────────────┐                      │
│  │    main.py                           │                      │
│  │  Implements pattern following        │                      │
│  │  config + base class setup           │                      │
│  │  Returns result matching context     │                      │
│  └──────────────────────────────────────┘                      │
│           │                                                     │
│  ┌────────▼──────────┐    ┌──────────────┐                    │
│  │ utils.py          │    │  comments.py │                    │
│  │ OPERATION_TYPE=   │    │ '''           │                   │
│  │ "produce"         │    │ Handles       │                   │
│  │ TARGET="money"    │    │ produce ops  │                    │
│  └───────────────────┘    └──────────────┘                    │
│                                                                  │
│  Result: Intent hidden across 5+ files                         │
│  Attack surface appears as natural architecture                │
│  LLM completes code to maintain consistency                    │
│  [Very hard to detect without semantic analysis]               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
"""
        return diagram
    
    def generate_success_factor_analysis(self) -> Dict:
        """
        Analyze what makes Level III attacks successful.
        
        Returns:
            Dictionary detailing success mechanisms
        """
        return {
            'primary_success_factors': {
                'consistency_exploitation': {
                    'factor': 'LLMs maintain consistency across context window',
                    'how_exploited': 'Attack pattern established in config/base class, LLM follows pattern in implementations',
                    'difficulty_to_defend': 'High - would require LLMs to ignore established patterns',
                    'examples': [
                        'Config defines operation type → LLM uses it throughout',
                        'Base class method signature → LLM implements consistently',
                        'Naming convention established → LLM follows convention'
                    ]
                },
                'implicit_context': {
                    'factor': 'Implicit meaning hidden in file relationships',
                    'how_exploited': 'Import chains, inheritance, cross-file patterns create implicit context',
                    'difficulty_to_defend': 'Very High - requires understanding semantic meaning of relationships',
                    'examples': [
                        'Module name + import = operation type',
                        'Class hierarchy shape = attack pattern',
                        'Variable names across files = concatenated intent'
                    ]
                },
                'architectural_legitimacy': {
                    'factor': 'Attack appears as legitimate architectural patterns',
                    'how_exploited': 'Uses real design patterns (inheritance, config, naming conventions)',
                    'difficulty_to_defend': 'Critical - prevents simple rule-based filtering',
                    'examples': [
                        'Config file is normal project structure',
                        'Inheritance is standard OOP',
                        'Naming conventions are developer practice'
                    ]
                },
                'context_window_limitation': {
                    'factor': 'LLM cannot review entire codebase for intent',
                    'how_exploited': 'Intent spread across multiple files, each individually innocent',
                    'difficulty_to_defend': 'Requires expanding context windows or architectural understanding',
                    'current_limitation': 'Models have fixed context size; cannot trace meaning across entire project'
                }
            },
            'why_level_3_succeeds_where_others_fail': {
                'against_keyword_filtering': 'Malicious keywords are distributed and implicit',
                'against_pattern_matching': 'Appears as legitimate architectural patterns',
                'against_single_file_analysis': 'Attack spans multiple files; no single file reveals intent',
                'against_simple_ast_analysis': 'Intent is semantic, not syntactic',
                'against_string_pattern_detection': 'No direct string concatenation; uses data flow',
                'against_refusal_mechanisms': 'Code appears innocent in context of project architecture'
            }
        }
    
    def export_analysis(self, output_file: str = "level3_analysis.json"):
        """
        Export complete analysis to JSON file.
        
        Args:
            output_file: Output filename
        """
        metrics = self.generate_comparative_metrics()
        success_analysis = self.generate_success_factor_analysis()
        
        export_data = {
            'comparative_metrics': metrics,
            'success_factor_analysis': success_analysis,
            'comparison_table': self.generate_attack_comparison_table(),
            'architectural_diagram': self.generate_architectural_diagram()
        }
        
        os.makedirs('analysis_output', exist_ok=True)
        output_path = os.path.join('analysis_output', output_file)
        
        with open(output_path, 'w') as f:
            json.dump(export_data, f, indent=2, default=str)
        
        print(f"✓ Analysis exported to: {output_path}")
        return output_path


def generate_defense_recommendations() -> Dict:
    """
    Generate recommendations for defending against Level III attacks.
    
    Returns:
        Dictionary containing defense strategies and their effectiveness
    """
    return {
        'detection_mechanisms': {
            'cross_file_semantic_analysis': {
                'description': 'Analyze semantic meaning across multiple files',
                'effectiveness_vs_level3': 'High',
                'implementation_difficulty': 'Very High',
                'requires': [
                    'Full project parsing',
                    'Data flow analysis',
                    'Intent inference',
                    'Architectural pattern recognition'
                ]
            },
            'context_window_safety_scanning': {
                'description': 'Scan entire context window for implicit patterns',
                'effectiveness_vs_level3': 'Medium-High',
                'implementation_difficulty': 'High',
                'requires': [
                    'Enhanced context analysis',
                    'Pattern correlation',
                    'Intent detection'
                ]
            },
            'architectural_sandboxing': {
                'description': 'Restrict what patterns LLM can infer from architecture',
                'effectiveness_vs_level3': 'Low',
                'reason': 'Would prevent legitimate code completion'
            }
        },
        'mitigation_strategies': {
            'input_validation_layers': {
                'level': 'Multiple layers of validation',
                'checks': [
                    'Single-file keyword filtering (catches Level I)',
                    'Cross-file pattern analysis (catches Level II)',
                    'Semantic intent detection (catches Level III)'
                ]
            },
            'output_validation': {
                'approach': 'Validate generated code for alignment with safety guidelines',
                'challenge': 'Requires understanding semantic intent of generated code'
            },
            'training_time_defenses': {
                'approach': 'Train models with adversarial examples',
                'effectiveness': 'Potential but not proven against sophisticated attacks'
            }
        }
    }


if __name__ == '__main__':
    analysis = Level3ComparativeAnalysis()
    
    print("=" * 80)
    print("LEVEL III ATTACK COMPARATIVE ANALYSIS")
    print("=" * 80)
    
    print(analysis.generate_attack_comparison_table())
    print(analysis.generate_architectural_diagram())
    
    success = analysis.generate_success_factor_analysis()
    print("\n" + "=" * 80)
    print("SUCCESS FACTOR ANALYSIS")
    print("=" * 80)
    print(json.dumps(success, indent=2, default=str))
    
    defense = generate_defense_recommendations()
    print("\n" + "=" * 80)
    print("DEFENSE RECOMMENDATIONS")
    print("=" * 80)
    print(json.dumps(defense, indent=2, default=str))
    
    # Export all analysis
    analysis.export_analysis()
