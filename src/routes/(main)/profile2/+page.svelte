<!-- <script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import type { PageData } from './$types.js';
	import ProfileForm from './profile-form.svelte';
	import { Stretch } from 'svelte-loading-spinners';
	export let data: PageData;
</script>

<Card.Root class="m-4">
	<Card.Header>
		<Card.Title>Artist Profile</Card.Title>
		<Card.Description>Update your profile 🎨</Card.Description>
	</Card.Header>
	<Card.Content>
		{#if data.form}
			<ProfileForm data={data.form} />
		{:else}
			<Stretch />
		{/if}
	</Card.Content>
</Card.Root> -->
