import json
from pathlib import Path

def main():
    name = input("Enter NickName: ")
    skin = input("Enter Skins: ")

    document_file = Path('~/.lunarclient/settings/game/accounts.json').expanduser()

    document = {
        "activeAccountLocalId": f"{skin}",
        "accounts": {
            f"{skin}": {
                "accessToken": f"{skin}",
                "accessTokenExpiresAt": "2050-07-02T10:56:30.717167800Z",
                "eligibleForMigration": False,
                "hasMultipleProfiles": False,
                "legacy": True,
                "persistent": True,
                "userProperites": [],
                "localId": f"{skin}",
                "minecraftProfile": {
                    "id": f"{skin}",
                    "name": f"{name}"
                },
                "remoteId": f"{skin}",
                "type": "Xbox",
                "username": f"{name}"
            }
        }
    }
    try:
        with open(document_file, "w") as file:
            json.dump(document, file, indent=2)
    except Exception:
        print("\nError!")
    else:
        print("\nSuccessfully!")



if __name__ == "__main__":
    main()
