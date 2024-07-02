import { error, redirect } from '@sveltejs/kit';
import { generateUsername } from '$lib/utils/generateUsername';

export const actions = {
    register: async ({ locals, request }) => {
        const body = Object.fromEntries(await request.formData());

        let username = generateUsername(body.name.split(' ').join('').tolowercase());

        try {
            await locals.pb.collection('users').create({ username, ...body })
            await locals.pb.collection('users').requestVerification(body.email)
        } catch (err) {
            console.log('Error: ', err)
            throw error(500, 'Error creating user')
        }

        throw redirect(303, '/')
}