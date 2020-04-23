package edu.virginia.cs.index.similarities;

import org.apache.lucene.search.similarities.BasicStats;
import org.apache.lucene.search.similarities.SimilarityBase;

public class OkapiBM25 extends SimilarityBase {
    /**
     * Returns a score for a single term in the document.
     *
     * @param stats
     *            Provides access to corpus-level statistics
     * @param termFreq
     * @param docLength
     */
    @Override
    protected float score(BasicStats stats, float termFreq, float docLength) {
    	//double k1=1.2;
    	//double k2=750;
    	//double b=0.75;
    	double s = 0.5;
    	//float firstTerm =  (float) Math.log((stats.getNumberOfDocuments()-stats.getDocFreq()+0.5)/(stats.getDocFreq()+0.5));
    	float firstTerm =  (float) Math.log((stats.getNumberOfDocuments()+1.0)/stats.getDocFreq());
    	//float secondTerm = (float) (((k1+1)*termFreq)/(k1*(1-b+b*(docLength/stats.getAvgFieldLength()))+termFreq));
    	float secondTerm = (float) ((termFreq)/((s+s*(docLength/stats.getAvgFieldLength()))+termFreq));
    	//Term Frequency in query is assumed to be one so the last term is simplified to be (k2+1)*1/(k2+1)=1
    	//float thirdTerm = (float) ((k2+1)*1/(k2+1)); 
    	float thirdTerm = (float) 1.0;
        return firstTerm*secondTerm*thirdTerm;
    }

    @Override
    public String toString() {
        return "Okapi BM25";
    }

}
