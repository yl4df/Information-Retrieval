package edu.virginia.cs.index.similarities;

import org.apache.lucene.search.similarities.BasicStats;
import org.apache.lucene.search.similarities.SimilarityBase;

public class PivotedLength extends SimilarityBase {
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
    	double s=0.75;
    	float firstTerm = (float)((1+Math.log(1+Math.log(termFreq)))/(1-s+s*(docLength/stats.getAvgFieldLength())));
    	float secondTerm = 1; // because term frequency in query is assumed to be 1
    	float thirdTerm = (float) (Math.log((stats.getNumberOfDocuments()+1)/stats.getDocFreq()));
        return firstTerm*secondTerm*thirdTerm;
    }

    @Override
    public String toString() {
        return "Pivoted Length Normalization";
    }

}
