package structures;

import java.util.HashMap;
import java.util.LinkedList;

public class Corpus {
	LinkedList<ReviewDoc> m_collection; // a list of review documents
	
	HashMap<String, Integer> m_dictionary; // dictionary of observed words in this corpus, word -> frequency
										   // you can use this structure to prepare the curve of Zipf's law
	
	public Corpus() {
		m_collection = new LinkedList<ReviewDoc>();
		m_dictionary = new HashMap<String, Integer>();
	}
	
	public int getCorpusSize() {
		return m_collection.size();
	}
	
	public int getDictionarySize() {
		return m_dictionary.size();	
	}
	public HashMap<String, Integer> getDictionary() {
		return m_dictionary;
	}
	
	public void addDoc(ReviewDoc doc) {
		m_collection.add(doc);
		
		/**
		 * INSTRUCTOR'S NOTE: based on the BoW representation of this document, you can update the m_dictionary content
		 * to maintain some global statistics here 
		 */
		
		for (String s: doc.m_BoW.keySet()) {
			if(!m_dictionary.containsKey(s)) {
				setWordCount(s,1);
			}
			else {
				int new_feq=getWordCount(s)+1;
				setWordCount(s,new_feq);
			}
		}
		

	}
	

	public ReviewDoc getDoc(int index) {
		if (index < getCorpusSize())
			return m_collection.get(index);
		else
			return null;
	}
	
	public int getWordCount(String term) {
		if (m_dictionary.containsKey(term))
			return m_dictionary.get(term);
		else
			return 0;
	}
	
	void setWordCount(String term, int count) {
		m_dictionary.put(term, count);
	}
}
