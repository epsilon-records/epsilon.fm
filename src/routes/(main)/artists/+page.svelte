<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Avatar from '$lib/components/ui/avatar';

	import type { PageData } from './$types.js';
	export let data: PageData;
</script>

<Card.Root class="m-4">
	<Card.Header>
		<Card.Title>Artists</Card.Title>
		<Card.Description>Member roster 🕺</Card.Description>
	</Card.Header>
	{#each data.artists as artist}
		<Card.Content>
			<div class="flex">
				<a href="/a/{artist.slug}">
					<Avatar.Root>
						<Avatar.Image src={artist.imageUrl} alt={artist.name} />
					</Avatar.Root></a
				><a href="/a/{artist.slug}"> <h1 class="pl-4 pt-2">{artist.name}</h1></a>
			</div>
		</Card.Content>
	{/each}
</Card.Root>
