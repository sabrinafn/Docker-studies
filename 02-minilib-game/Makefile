SERVICE = mlxgame

build:
	@echo "Building the Docker image for $(SERVICE)..."
	@docker compose build $(SERVICE) > /dev/null 2>&1
	@echo "Docker image built successfully."

run:
	@echo "Starting the container in the background..."
	@docker compose up -d $(SERVICE) > /dev/null 2>&1
	@echo "Container is now running in the background."

map:
ifndef MAP
	@echo "Error: you must provide a map file."
	@echo "Example: make map MAP=map01"
	@exit 1
endif
	@echo "Running the game with map: $(MAP)..."
	docker compose exec $(SERVICE) ./so_long maps/$(MAP).ber
	@echo "Game execution finished."

clean:
	@echo "Stopping and removing containers, images, and volumes..."
	@docker compose down --rmi all -v --remove-orphans > /dev/null 2>&1
	@echo "Clean up completed."

help:
	@echo ""
	@echo "Available commands:"
	@echo ""
	@echo "  make build          -> build the Docker image"
	@echo "  make run            -> start the container in background"
	@echo "  make map MAP=map    -> run the game with the chosen map"
	@echo "                         ex.: make map MAP=map42"
	@echo "  make clean          -> remove containers/images/volumes"
	@echo "  make help           -> show this help"
	@echo ""
	@echo "Available maps:"
	@echo "   - map00"
	@echo "   - map01"
	@echo "   - map03"
	@echo "   - map04"
	@echo "   - map05"
	@echo "   - map42"
	@echo ""
	@echo "Recommended workflow to avoid initial delay:"
	@echo "  Step 1 - Build the Docker image (only once):"
	@echo "      > make build"
	@echo "  Step 2 - Start the container in background (only once):"
	@echo "      > make run"
	@echo "  Step 3 - Run the game with a map:"
	@echo "      > make map MAP=maps/map42.ber"
	@echo ""
