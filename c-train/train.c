#include <stdio.h>

#include "fann.h"

int main()
{
	const unsigned int num_layers = 3;
	const unsigned int num_neurons_hidden = 35;
	const float desired_error = (const float) 0.001;
	const unsigned int max_epochs = 2000;
	const unsigned int epochs_between_reports = 1;
	struct fann *ann;
	struct fann_train_data *train_data, *test_data;

	unsigned int i = 0;

	printf("Creating network.\n");

	train_data = fann_read_train_from_file("../data/traindata.txt");

	ann = fann_create_standard(num_layers,
					  train_data->num_input, num_neurons_hidden, train_data->num_output);

	printf("Training network.\n");

	fann_set_activation_function_hidden(ann, FANN_SIGMOID_SYMMETRIC_STEPWISE);
	fann_set_activation_function_output(ann, FANN_SIGMOID_STEPWISE);

	/*fann_set_training_algorithm(ann, FANN_TRAIN_INCREMENTAL); */

	fann_train_on_data(ann, train_data, max_epochs, epochs_between_reports, desired_error);

	printf("Saving network.\n");

	fann_save(ann, "../structs/network.4");

	fann_destroy_train(train_data);
	fann_destroy(ann);

	return 0;
}
