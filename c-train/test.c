#include<fann.h>
#include<stdio.h>
#include<string.h>

#define WORDLEN 3

fann_type ret_string(struct fann *ann, char *s) {
	fann_type *calc_out;
	fann_type input[WORDLEN*26];
	int i,j;

	for (j=0;j<strlen(s);j++)
		for (i=0;i<26;i++) {
			if (s[j]-'a' == i) 
				input[(j*26) + i] = 1;
			else
				input[(j*26) + i] = 0;
	}
	calc_out=fann_run(ann,input);
	return calc_out[0];
}

fann_type val_word(struct fann *ann, char *s) {
	char snipp[WORDLEN+1];
	int i,j,m=0;
	fann_type count=1, rt, avg=0;
	snipp[WORDLEN]=0;
	for (i=0;i <= (strlen(s)-WORDLEN);i++) {
		for(j=0;j<WORDLEN;j++) 
			snipp[j]=s[j+i];
		rt = ret_string(ann,snipp);
		//printf("%s : %f\n",snipp,rt);
		count = count * rt;
		m++;
		avg = avg + rt;
	}
	avg = avg/m;
	//fprintf(stdout,"Final: count: %f, avg: %f\n",count, avg);

	// value function
	return count;
}

main(int argc, char **argv) {
	struct fann *ann = fann_create_from_file("../structs/network.4");
	printf("%f",val_word(ann,argv[1]));
}
