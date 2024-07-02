import PocketBase from 'pocketbase'
import { serializeNonPOJO } from './lib/utils';

export const handle = async ({ event, resolve }) => {
    event.locals.pb = new PocketBase('epsilon.pockethost.io');
    event.locals.pb.authStore.loadFromCookie(event.request.headers.get('cookie') || '');

    if (event.locals.pb.authStore.isValid) {
        event.locals.user = serializeNonPOJO(event.locals.pb.authStore.model);
    } else {
        event.locals.user = undefined;
    }

    const response = await resolve(event);

    response.headers.set('set-cookie', event.locals.pb.authStore.exportToCookie()); 

    return response;
    