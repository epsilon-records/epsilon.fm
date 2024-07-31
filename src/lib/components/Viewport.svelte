<script lang="ts">
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
</script>

<main class="grid flex-1 p-4">
	<SignedIn let:user>
		<div class="grid auto-rows-max items-start justify-center gap-4 md:gap-8 lg:col-span-2">
			<div class="grid grid-cols-1 gap-8">
				<slot name="content" />
			</div>
		</div>
	</SignedIn>
</main>
