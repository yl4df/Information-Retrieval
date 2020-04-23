package edu.virginia.cs.searcher;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;

import edu.virginia.cs.analyzer.TextAnalyzer;
import opennlp.tools.util.InvalidFormatException;
import structures.Corpus;
import structures.ReviewDoc;

public class DocSearcher {
	Corpus m_corpus;
	TextAnalyzer m_tAnalyzer;
	
	public DocSearcher(Corpus corpus, String tokenizerModel) throws InvalidFormatException, FileNotFoundException, IOException {
		m_corpus = corpus;
		m_tAnalyzer = new TextAnalyzer(tokenizerModel);
	}
	
	//brute force search against the whole corpus
	public ReviewDoc[] search(String query) {
		String[] queryTerms = m_tAnalyzer.tokenize(query);
		
		ArrayList<ReviewDoc> results = new ArrayList<ReviewDoc>();
		long currentTime = System.currentTimeMillis();
		for(int i=0; i<m_corpus.getCorpusSize(); i++) {
			ReviewDoc doc = m_corpus.getDoc(i);			
			int matchCount = 0;
			for(String term:queryTerms) {
				/**
				 * INSTRUCTOR'S NOTE: match the processed query terms against each document's BoW representation
				 * Find the document that matches at least one query key word
				 */
				if(doc.getBoW().containsKey(term)) {
					matchCount += 1;
				}
			}
			
			//exact match of all query terms
			if (matchCount == queryTerms.length)
				results.add(doc);
		}
		
		long timeElapsed = System.currentTimeMillis() - currentTime;
		System.out.format("[Info]%d documents returned for query [%s] in %.3f seconds\n", results.size(), query, timeElapsed/1000.0);
		return results.toArray(new ReviewDoc[results.size()]);
	}
}
