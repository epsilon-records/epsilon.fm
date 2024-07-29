<script lang="ts">
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
</script>

<main
	class="grid flex-1 items-start gap-4 p-4 sm:px-6 sm:py-0 md:gap-8 lg:grid-cols-3 xl:grid-cols-3"
>
	<SignedIn let:user>
		<div class="grid auto-rows-max items-start gap-4 md:gap-8 lg:col-span-2">
			<div class="grid gap-4 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-2 xl:grid-cols-4">
				<slot name="topLeft" />
				<slot name="topCenter" />
				<slot name="topRight" />
			</div>
			<slot name="content" />
		</div>
		<div>
			<slot name="sidebar" />
		</div>
	</SignedIn>
</main>
