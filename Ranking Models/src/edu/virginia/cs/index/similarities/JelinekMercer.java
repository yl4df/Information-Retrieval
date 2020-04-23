package edu.virginia.cs.index.similarities;

import org.apache.lucene.search.similarities.BasicStats;
import org.apache.lucene.search.similarities.LMSimilarity;

public class JelinekMercer extends LMSimilarity {

    private LMSimilarity.DefaultCollectionModel model; // this would be your reference model
    private float queryLength = 0; // will be set at query time automatically

    public JelinekMercer() {
        model = new LMSimilarity.DefaultCollectionModel();
    }

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
    	float lambda = (float) 0.1;
    	float alpha = lambda;
    	float smoothing = (float)((1 - lambda) * (termFreq/docLength) + lambda * model.computeProbability(stats));
    	float score = (float) (Math.log(smoothing/(alpha*model.computeProbability(stats)))+ Math.log(alpha)*queryLength);
        return score;
    }

    @Override
    public String toString() {
        return getName();
    }

    @Override
    public String getName() {
        return "Jelinek-Mercer Language Model";
    }

    public void setQueryLength(float length) {
        queryLength = length;
    }

}
