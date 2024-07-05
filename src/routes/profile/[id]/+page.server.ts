import type { PageServerLoad, Actions } from '../$types.js';
import { fail } from '@sveltejs/kit';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { artistSchema } from './schema';
import { db } from '$lib/db';
import { artist } from '$lib/db/schema';
import { eq } from 'drizzle-orm';

export const load: PageServerLoad = async ({ locals }) => {
	const authId = locals?.session?.userId ?? null;
	const orgId = locals?.session?.claims?.org_id ?? null;
	console.log(authId);
	console.log(orgId);
	if (!authId || !orgId) {
		fail(500); // TODO: cleanup
	}
	const data = await db.select().from(artist).where(eq(artist.orgId, orgId));
	console.log(data);
	const form = await superValidate({ data }, zod(artistSchema));
	form.data.orgId = orgId;
	return {
		authId: authId,
		orgId: orgId,
		form: form
	};
};

export const actions: Actions = {
	default: async (event) => {
		const form = await superValidate(event, zod(artistSchema));
		console.log(form);
		if (!form.valid) {
			return fail(400, {
				form
			});
		}
		try {
			await db
				.insert(artist)
				.values(form.data)
				.onConflictDoUpdate({
					target: artist.orgId,
					set: { stageName: form.data.stageName }
				});
		} catch (error) {
			console.log(error);
		}
		return {
			form
		};
	}
};
