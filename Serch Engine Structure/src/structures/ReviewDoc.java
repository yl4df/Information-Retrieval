/**
 * 
 */
package structures;

import java.util.Date;
import java.util.HashMap;

/**
 * @author Hongning Wang
 * Basic data structure for a Yelp review document
 */
public class ReviewDoc {
	String m_author; //author name
	String m_docID; //unique review id
	double m_rating; //numerical rating of the review
	String m_content; //review text content
	Date m_date; //date when the review was published
	String m_authorLocation; //author's registered location
	
	/**
	 * INSTRUCTOR'S NOTE: Your bag-of-word representation of this document
	 * HashMap is an example, and you are free to use any reasonable data structure for this purpose
	 */
	HashMap<String, Integer> m_BoW=new HashMap<String, Integer>(); //word -> frequency
	
	public ReviewDoc(String docID, String author) {
		m_docID = docID;
		m_author = author;
	}
	
	public void setAuthor(String author) {
		m_author = author;
	}
	
	public String getAuthor() {
		return m_author;
	}
	
	public void setDocID(String docID) {
		m_docID = docID;
	}
	
	public String getDocID() {
		return m_docID;
	}
	
	public void setRating(double rating) {
		m_rating = rating;
	}
	
	public double getRating() {
		return m_rating;
	}
	
	public void setContent(String content) {
		m_content = content;
	}
	
	public String getContent() {
		return m_content;
	}
	
	public void setDate(Date date) {
		m_date = date;
	}
	
	public Date getDate() {
		return m_date;
	}
	
	public void setAuthorLocation(String authorLoc) {
		m_authorLocation = authorLoc;
	}
	
	public String getAuthorLocation() {
		return m_authorLocation;
	}
	
	public void setBoW(String[] tokens) {
		/**
		 * INSTRUCTOR'S NOTE: please construct your bag-of-word representation of this document based on the processed document content
		 */
		
		for(String token:tokens) {

			if(!m_BoW.containsKey(token)) {
				m_BoW.put(token, 1);
			}
			else {
				int new_feq=m_BoW.get(token)+1;
				m_BoW.replace(token, new_feq);
			}
		}

	}
	
	public HashMap<String, Integer> getBoW(){
		return m_BoW;
	}
	
	//check whether the document contains the query term
	public boolean contains(String term) {
		return m_BoW.containsKey(term);
	}
	
	//return the frequency of query term in this document 
	public int counts(String term) {
		if (contains(term))
			return m_BoW.get(term);
		else 
			return 0;
	}
}
