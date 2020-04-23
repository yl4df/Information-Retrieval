package runners;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.util.HashMap;

import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.MultiFields;
import org.apache.lucene.index.Term;
import org.apache.lucene.index.Terms;
import org.apache.lucene.index.TermsEnum;
import org.apache.lucene.store.FSDirectory;

import edu.virginia.cs.analyzer.DocAnalyzer;
import edu.virginia.cs.index.Indexer;
import edu.virginia.cs.index.Searcher;
import edu.virginia.cs.searcher.DocSearcher;

public class Main {

	//The main entrance to test various functions 
	public static void main(String[] args) {
		try {
	
			DocAnalyzer analyzer = new DocAnalyzer("data/models/en-token.bin");
			analyzer.LoadDirectory("data/yelp/60", ".json");

			
			/*
			String query1 = "general chicken";
			String query2 ="fried chicken";
			String query3 ="BBQ sandwiches";
			String query4 ="mashed potatoes";
			String query5 ="Grilled Shrimp Salad";
			String query6 ="lamb Shank";
			String query7 ="Pepperoni pizza";
			String query8 ="brussel sprout salad";
			String query9 ="FRIENDLY STAFF";
			String query10 ="Grilled Cheese";			
 */
//			//using brute-force strategy to scan through the whole corpus
			/*
			DocSearcher bruteforceSearcher = new DocSearcher(analyzer.getCorpus(), "data/models/en-token.bin");
			bruteforceSearcher.search(query1);
			bruteforceSearcher.search(query2);
			bruteforceSearcher.search(query3);
			bruteforceSearcher.search(query4);
			bruteforceSearcher.search(query5);
			bruteforceSearcher.search(query6);
			bruteforceSearcher.search(query7);
			bruteforceSearcher.search(query8);
			bruteforceSearcher.search(query9);
			bruteforceSearcher.search(query10);
			*/
			
			//create inverted index
			Indexer.index("data/indices", analyzer.getCorpus());
			
			
			IndexReader reader = DirectoryReader.open(FSDirectory.open(new File("data/indices")));//using your own index path
			Terms terms = MultiFields.getTerms(reader, "content");//get reference to all the indexed terms in the content field
			TermsEnum termsEnum = terms.iterator(null);
			while (termsEnum.next()!=null) {//iterate through all terms
			    Term t = new Term("content", termsEnum.term());//map it to the corresponding field
			    System.out.format("%s\t%d\t%d\n", t, termsEnum.docFreq(), reader.totalTermFreq(t));//print term text, DF and TTF        
			}
			
			//search in the inverted index
			/*
			Searcher indexSearcher = new Searcher("data/indices");
			indexSearcher.search(query1);
			indexSearcher.search(query2);
			indexSearcher.search(query3);
			indexSearcher.search(query4);
			indexSearcher.search(query5);
			indexSearcher.search(query6);
			indexSearcher.search(query7);
			indexSearcher.search(query8);
			indexSearcher.search(query9);
			indexSearcher.search(query10);
			*/
			
		} catch (IOException e) {
			e.printStackTrace();
			}
	}

}
