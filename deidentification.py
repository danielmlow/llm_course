!pip install presidio-analyzer
!pip install presidio-anonymizer
!python -m spacy download en_core_web_lg

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from tqdm import tqdm
anonymized_text_all = []


for text in tqdm(df['Transcript'].tolist()):
    

    # Set up the engine, loads the NLP module (spaCy model by default) 
    # and other PII recognizers
    analyzer = AnalyzerEngine()

    # Call analyzer to get results
    results = analyzer.analyze(text=text,
                            entities=["PERSON","NAME", "PHONE_NUMBER","NUMBER"], #You could add LOCATION
                            language='en')
    # print(results)

    # Analyzer results are passed to the AnonymizerEngine for anonymization

    anonymizer = AnonymizerEngine()

    anonymized_text = anonymizer.anonymize(text=text,analyzer_results=results)
    anonymized_text_all.append(text)

