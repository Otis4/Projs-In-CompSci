


public class MadlibText{
	// the part of speech: will change w/ input
	private String partOfSpeech;
	//text before part of speech
	private String preText;
	// check for part of speech for ending text of madlib
	private boolean poSCheck;
	public MadlibText(String partOfSpeech, String preText){
		this.preText = preText;
		this.partOfSpeech = partOfSpeech;
		poSCheck = true;
	}
	public MadlibText(String partOfSpeech, String preText, boolean poSCheck){
		this.preText = preText;
		this.partOfSpeech = partOfSpeech;
		this.poSCheck = poSCheck;
	}
	
	
	
	
	
	
	
	
	
	
}