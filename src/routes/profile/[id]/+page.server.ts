import type { PageServerLoad, Actions } from '../$types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { artistSchema } from './schema';
import { db } from '$lib/db';

export const load: PageServerLoad = async ({ locals }) => {
	// Get the userId from auth() -- if null, the user is not signed in

	const userId = locals.session.userId;
	const orgId = locals.session.claims.ordId;

	const result = await db.query.artist.findFirst({ where: { id: userId } });
	console.log(result);

	return {
		userId: userId,
		orgId: orgId,
		form: await superValidate(zod(artistSchema))
	};
};

export const actions: Actions = {
	default: async (event) => {
		const form = await superValidate(event, zod(artistSchema));
		if (!form.valid) {
			return fail(400, {
				form
			});
		}
		return {
			form
		};
	}
};
