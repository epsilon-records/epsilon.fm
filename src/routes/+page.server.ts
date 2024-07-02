import { z } from 'zod';
import { superValidate } from 'sveltekit-superforms/server';
import { zod } from 'sveltekit-superforms/adapters';

const schema = z.object({
	name: z.string().default('Hello world!'),
	email: z.string().email()
});

export const load = async () => {
	const form = await superValidate(zod(schema));

	// Always return { form } in load functions
	return { form };
};
