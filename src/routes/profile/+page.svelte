<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import type { PageData } from './$types.js';
	import ProfileForm from './ProfileForm.svelte';
	import UserProfile from 'clerk-sveltekit/client/UserProfile.svelte';
	export let data: PageData;
	export let clerk;
</script>

<Card.Root class="m-4">
	<Card.Header>
		<Card.Title>Artist Profile</Card.Title>
		<Card.Description>Update your profile 🎨</Card.Description>
	</Card.Header>
	<Card.Content>
		<ProfileForm {clerk} data={data.form} />
	</Card.Content>
</Card.Root>
