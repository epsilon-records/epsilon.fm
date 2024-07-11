<script lang="ts">
	import * as Card from '$lib/components/ui/card';
	import * as Accordion from '$lib/components/ui/accordion';
</script>

<Card.Root class="m-4">
	<Card.Header>
		<Card.Title>FAQ</Card.Title>
		<Card.Description>Frequently Asked Questions ❓</Card.Description>
	</Card.Header>
	<Card.Content>
		<Accordion.Root class="w-full self-center sm:max-w-[100%]">
			<Accordion.Item value="item-1">
				<Accordion.Trigger>Is it free?</Accordion.Trigger>
				<Accordion.Content>No.</Accordion.Content>
			</Accordion.Item>
			<Accordion.Item value="item-2">
				<Accordion.Trigger>Do you deliver to Spotify?</Accordion.Trigger>
				<Accordion.Content>Yes.</Accordion.Content>
			</Accordion.Item>
		</Accordion.Root>
	</Card.Content>
</Card.Root>
