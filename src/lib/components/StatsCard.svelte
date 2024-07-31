<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import type { MusicfetchArtist } from '$lib/consumer/musicfetch';
	import { Badge } from '$lib/components/ui/badge';
	import spotifyLogo from '$lib/images/spotify-logo.svg';
	import appleMusicLogo from '$lib/images/apple-music-logo.svg';
	import youtubeLogo from '$lib/images/youtube-logo.svg';
	import soundcloudLogo from '$lib/images/soundcloud-logo.svg';
	import deezerLogo from '$lib/images/deezer-logo.svg';
	import shazamLogo from '$lib/images/shazam-logo.svg';
	import tidalLogo from '$lib/images/tidal-logo.svg';

	export let artistInfo: MusicfetchArtist | null = null;
	export let error: string | null = null;

	function getFirstArtist(artists: MusicfetchArtist[]): MusicfetchArtist | null {
		return artists && artists.length > 0 ? artists[0] : null;
	}

	const serviceLogo: { [key: string]: string } = {
		spotify: spotifyLogo,
		applemusic: appleMusicLogo,
		youtube: youtubeLogo,
		soundcloud: soundcloudLogo,
		deezer: deezerLogo,
		shazam: shazamLogo,
		tidal: tidalLogo
	};
</script>

<SignedIn let:user>
	<Card.Root class="sm:col-span-2">
		{#if error}
			<Card.Header>
				<Card.Title class="text-2xl ">⚠️ Error</Card.Title>
			</Card.Header>
			<Card.Content>
				<Badge variant="destructive">{error}</Badge>
			</Card.Content>
		{:else if artistInfo}
			{@const firstArtist = getFirstArtist(artistInfo?.artists)}
			<Card.Header class="pb-3">
				{#if firstArtist}
					<Card.Title class="text-2xl">{firstArtist.name}</Card.Title>
					<Card.Description class="max-w-lg text-balance leading-relaxed">
						<img
							src={firstArtist.image.url}
							alt={firstArtist.name}
							class="m-4 h-32 w-32 rounded-full object-cover"
						/>
					</Card.Description>
				{:else}
					<Card.Title class="text-2xl">Warning</Card.Title>
					<Card.Description>No artist found in the provided information.</Card.Description>
				{/if}
			</Card.Header>
			<Card.Content>
				{#if firstArtist}
					<div class="space-y-4">
						{#if firstArtist.description}
							<p>{firstArtist.description}</p>
						{:else}
							<p class="text-gray-500">No biography available for this artist.</p>
						{/if}

						{#if Object.entries(firstArtist.services).length > 0}
							<ul class="flex space-x-4">
								{#each Object.entries(firstArtist.services) as [serviceType, service]}
									<li>
										<a href={service.link} target="_blank" rel="noopener noreferrer">
											{#if serviceLogo[serviceType.toLowerCase()]}
												<img
													src={serviceLogo[serviceType.toLowerCase()]}
													alt={`${serviceType} logo`}
													class="h-16 w-32"
												/>
											{:else}
												<span
													class="flex h-16 w-32 items-center justify-center rounded-full bg-gray-200 text-xs"
												>
													{serviceType.slice(0, 2).toUpperCase()}
												</span>
											{/if}
										</a>
									</li>
								{/each}
							</ul>
						{:else}
							<p class="text-gray-500">No services information available for this artist.</p>
						{/if}
					</div>
				{:else}
					<p>No artist information available.</p>
				{/if}
			</Card.Content>
		{:else}
			<Card.Header>
				<Card.Title class="text-2xl">Loading</Card.Title>
			</Card.Header>
			<Card.Content>
				<p>Fetching artist information...</p>
			</Card.Content>
		{/if}
	</Card.Root>
</SignedIn>
