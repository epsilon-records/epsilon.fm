<script lang="ts">
	import { Badge } from '$lib/components/ui/badge';
	import * as Card from '$lib/components/ui/card';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import type { MusicfetchArtist } from '$lib/consumer/musicfetch';

	export let trackInfo: { artists: MusicfetchArtist[] };

	function getGreeting(firstName: string | null | undefined): string {
		const hour = new Date().getHours();
		let greeting = '';

		if (hour < 12) {
			greeting = 'Good morning';
		} else if (hour < 18) {
			greeting = 'Good afternoon';
		} else {
			greeting = 'Good evening';
		}

		return firstName ? `${greeting}, ${firstName}` : greeting;
	}

	function getFirstArtist(trackInfo: { artists: MusicfetchArtist[] }): MusicfetchArtist | null {
		return trackInfo?.artists?.[0] || null;
	}
</script>

<SignedIn let:user>
	{@const firstArtist = getFirstArtist(trackInfo)}

	<Card.Root class="sm:col-span-2">
		{#if firstArtist}
			<Card.Header class="pb-3">
				<Card.Title class="text-4xl">{firstArtist.name}</Card.Title>
				<Card.Description class="max-w-lg text-balance leading-relaxed">
					<img
						src={firstArtist.image.url}
						alt={firstArtist.name}
						class="h-32 w-32 rounded-full object-cover"
					/>
				</Card.Description>
			</Card.Header>
		{/if}
		<Card.Content>
			{#if firstArtist}
				<div class="space-y-4">
					{#if firstArtist.description}
						<p>{firstArtist.description}</p>
					{/if}

					{#each Object.entries(firstArtist.services) as [serviceType, service]}
						<li>{serviceType}: <a href={service.link}>{service.id}</a></li>
					{/each}
				</div>
			{:else}
				<p>No artist information available.</p>
			{/if}
		</Card.Content>
	</Card.Root>
</SignedIn>
