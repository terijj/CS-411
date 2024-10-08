from typing import Any, Optional

class Animal:
    def __init__(self,
                 animal_id: int,
                 species: str,
                 age: Optional[int] = None,
                 health_status: Optional[str] = None,
                 location: Optional[str] = None) -> None:
        
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.health_status = health_status
        self.location = location

    def update_animal_details(self, **kwargs: Any) -> None:
    
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_animal_details(self) -> dict:
        
        return {
            'animal_id': self.animal_id,
            'species': self.species,
            'age': self.age,
            'health_status': self.health_status,
            'location': self.location
        }

