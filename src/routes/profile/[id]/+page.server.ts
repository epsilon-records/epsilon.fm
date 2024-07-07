import type { PageServerLoad, Actions } from '../$types.js';
import { superValidate } from 'sveltekit-superforms';
import { zod } from 'sveltekit-superforms/adapters';
import { artistSchema } from './schema';
import { db } from '$lib/db';
import { artist } from '$lib/db/schema';
import { eq } from 'drizzle-orm';
import { clerkClient } from '@clerk/clerk-sdk-node';
import { error } from '@sveltejs/kit';

export const load: PageServerLoad = async ({ locals }) => {
	const organizationId = locals.session.claims.org_id ?? null;
	const response = await clerkClient.organizations.getOrganization({ organizationId });
	const organizationName = response.name ?? null;
	const organizationSlug = response.slug ?? null;
	if (!organizationId || !organizationName || !organizationSlug) {
		error(500, 'Organization not selected');
	}
	let form = await superValidate(zod(artistSchema));
	const data = await db.select().from(artist).where(eq(artist.orgId, organizationId));
	if (data.length != 0) {
		form = await superValidate(data[0], zod(artistSchema));
		console.log(form);
		form.data.orgId = organizationId;
		form.data.stageName = organizationName;
		form.data.orgSlug = organizationSlug;
		console.log(form);
	}
	return {
		form: form
	};
};

export const actions: Actions = {
	default: async (event) => {
		console.log('TEST');
		const form = await superValidate(event, zod(artistSchema));
		console.log(form);
		if (!form.valid) {
			console.log(form.errors);
			return fail(400, {
				form
			});
		}
		console.log('hellow');
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
