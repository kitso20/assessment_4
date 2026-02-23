import pytest
from summative import *
import json
import copy


class TestSummative():



    ###################Question 1###################################
    @pytest.mark.parametrize("input_ids, expected_output", [
        (['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7'],
        [['ID1', 'ID2', 'ID3', 'ID4', 'ID5'], ['ID6', 'ID7']]),

        (['ID1', 'ID2', 'ID3', 'ID4', 'ID5'],
        [['ID1', 'ID2', 'ID3', 'ID4', 'ID5']]),

        (['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6', 'ID7', 'ID8', 'ID9', 'ID10'],
        [['ID1', 'ID2', 'ID3', 'ID4', 'ID5'], ['ID6', 'ID7', 'ID8', 'ID9', 'ID10']]),

        (['ID1', 'ID2', 'ID3'], [['ID1', 'ID2', 'ID3']]),

        (['ID1'], [['ID1']]),

        ([], []),

        (['1', '2', '3', '4', '5', '6'], [['1', '2', '3', '4', '5'], ['6']]),

        (['ID10', 'ID5', 'ID3', 'ID8', 'ID1', 'ID7'],
        [['ID10', 'ID5', 'ID3', 'ID8', 'ID1'], ['ID7']]),
    ])
    def test_batch_api_dispatcher_logic(self, input_ids, expected_output):
        assert batch_api_dispatcher(input_ids) == expected_output


    def test_batch_api_dispatcher_constraint_enforced(self):
        user_ids = [f"ID{i}" for i in range(1, 50)]
        result = batch_api_dispatcher(user_ids)
        for batch in result:
            assert len(batch) <= 5, f"Batch exceeded limit: {batch}"



    def test_batch_api_dispatcher_no_data_loss(self):
        user_ids = [f"ID{i}" for i in range(1, 23)]
        result = batch_api_dispatcher(user_ids)
        flattened = [item for batch in result for item in batch]
        assert flattened == user_ids


    def test_batch_api_dispatcher_no_duplicates(self):
        user_ids = [f"ID{i}" for i in range(1, 18)]
        result = batch_api_dispatcher(user_ids)
        flattened = [item for batch in result for item in batch]
        assert len(flattened) == len(set(flattened))


    def test_batch_api_dispatcher_order_preserved(self):
        user_ids = [f"ID{i}" for i in range(100, 115)]
        result = batch_api_dispatcher(user_ids)
        flattened = [item for batch in result for item in batch]
        assert flattened == user_ids



    def test_batch_api_dispatcher_returns_list_of_lists(self):
        result = batch_api_dispatcher(['ID1', 'ID2', 'ID3', 'ID4', 'ID5', 'ID6'])
        assert isinstance(result, list)
        for batch in result:
            assert isinstance(batch, list)


    def test_batch_api_dispatcher_empty_returns_list(self):
        result = batch_api_dispatcher([])
        assert result == []
        assert isinstance(result, list)



    def test_batch_api_dispatcher_immutability(self):
        original = ['A', 'B', 'C', 'D', 'E', 'F']
        original_copy = original.copy()
        batch_api_dispatcher(original)
        assert original == original_copy, "Input list was mutated!"



    def test_batch_api_dispatcher_large_scale(self):
        large_input = [f"ID{i}" for i in range(10000)]
        result = batch_api_dispatcher(large_input)

        assert len(result) == 2000
        assert all(len(batch) == 5 for batch in result)

        flattened = [item for batch in result for item in batch]
        assert flattened == large_input

    ###################Question 2###################################

    @pytest.mark.parametrize("results, expected", [
        ([], 0),
        (['L'], 0),
        (['W'], 1),
        (['L', 'L', 'L', 'L', 'L'], 0),
        (['W', 'W', 'W', 'W', 'W'], 5),

        (['W', 'W', 'W', 'L', 'L', 'L'], 3),

        (['L', 'L', 'L', 'W', 'W', 'W'], 3),

        (['L', 'W', 'W', 'W', 'W', 'L'], 4),

        (['W', 'W', 'L', 'W', 'W', 'W', 'L', 'W', 'W'], 3),
        (['W', 'L', 'W', 'W', 'L', 'W', 'W', 'W'], 3),
        (['L', 'W', 'W', 'W', 'W', 'W', 'W', 'L', 'W'], 6),

        (['W', 'L', 'W', 'L', 'W', 'L', 'W'], 1),
        (['L', 'W', 'L', 'W', 'L', 'W'], 1),

        (['W', 'W', 'L', 'W', 'W', 'L', 'W', 'W'], 2),

        (['L', 'W', 'L', 'W', 'W', 'L', 'W', 'W', 'W', 'L', 'L', 'W', 'W', 'W', 'L', 'W', 'W'], 3),
        (['W', 'W', 'L', 'L', 'W', 'W', 'W', 'W', 'L', 'W'], 4),
    ])
    def test_winning_streak_logic(self, results, expected):
        assert winning_streak(results) == expected



    @pytest.mark.parametrize("streak_length", [1, 2, 5, 10, 20, 50, 99, 100])
    def test_winning_streak_exact_streak_surrounded_by_losses(self, streak_length):
    
        results = ['L', 'L'] + ['W'] * streak_length + ['L', 'L']
        assert winning_streak(results) == streak_length

    @pytest.mark.parametrize("streak_length", [1, 3, 7, 13, 25, 50])
    def test_winning_streak_two_streaks_second_is_longer(self, streak_length):
        short_streak = ['W'] * (streak_length - 1) if streak_length > 1 else []
        long_streak = ['W'] * streak_length
        results = short_streak + ['L'] + long_streak
        assert winning_streak(results) == streak_length

    @pytest.mark.parametrize("streak_length", [1, 3, 7, 13, 25, 50])
    def test_winning_streak_two_streaks_first_is_longer(self, streak_length):
        long_streak = ['W'] * streak_length
        short_streak = ['W'] * max(1, streak_length - 1)
        results = long_streak + ['L'] + short_streak
        assert winning_streak(results) == streak_length

    @pytest.mark.parametrize("num_blocks, block_size", [
        (5, 3), (10, 4), (20, 2), (100, 1), (3, 10)
    ])
    def test_winning_streak_repeating_blocks(self, num_blocks, block_size):
        results = (['W'] * block_size + ['L']) * num_blocks
        assert winning_streak(results) == block_size

    def test_winning_streak_large_scale_known_streak(self):
        filler = (['W', 'W', 'L']) * 100          
        injected = ['W'] * 37
        results = filler + ['L'] + injected + ['L'] + filler
        assert winning_streak(results) == 37

    def test_winning_streak_large_all_wins(self):
        results = ['W'] * 10000
        assert winning_streak(results) == 10000

    def test_winning_streak_large_all_losses(self):
        results = ['L'] * 10000
        assert winning_streak(results) == 0



    def test_winning_streak_returns_int(self):
        assert isinstance(winning_streak(['W', 'L', 'W']), int)

    def test_winning_streak_returns_zero_not_none(self):
        result = winning_streak([])
        assert result == 0
        assert isinstance(result, int)

    def test_winning_streak_immutability(self):
        original = ['W', 'L', 'W', 'W', 'L']
        copy = original.copy()
        winning_streak(original)
        assert original == copy, "Input list was mutated!"


    ###################Question 3###################################

    @pytest.mark.parametrize("temperatures, expected", [
        ([1, 3, 7, 1, 2, 6, 3, 2, 1], [7, 6]),

        ([1, 2, 3, 4, 5], []),
        ([9, 7, 5, 3, 1], []),

        ([2, 4, 6, 4, 2], [6]),

        ([5, 10, 5, 10, 5, 10, 5], [10, 10, 10]),
        ([1, 2, 1, 2, 1, 2, 1], [2, 2, 2]),

        ([1, 3, 5, 5, 3, 1], []),
        ([1, 5, 5, 1], []),

        ([10, 5, 1, 5, 10], []),

        ([2, 5, 3, 6, 4, 7, 1], [5, 6, 7]),

        ([3, 8, 3, 8, 3], [8, 8]),
        ([6, 4, 6, 4, 6, 4, 6], [6, 6]),

        ([1, 5, 2, 8, 3], [5, 8]),

        ([-5, -2, -8, -1, -3], [-2, -1]),

        ([-3, 2, -1, 5, 3], [2, 5]),
    ])
    def test_peak_finder_logic(self, temperatures, expected):
        assert peak_finder(temperatures) == expected



    @pytest.mark.parametrize("temperatures, reason", [
        ([], 'empty list'),
        ([5], 'single element — no neighbours'),
        ([5, 10], 'two elements — no middle element possible'),
        ([5, 10, 10], 'right plateau — not strictly greater than right neighbour'),
        ([10, 10, 5], 'left plateau — not strictly greater than left neighbour'),
        ([3, 3, 3], 'all equal'),
        ([1, 3, 3, 1], 'plateau in middle'),
    ])
    def test_peak_finder_returns_empty(self, temperatures, reason):
        result = peak_finder(temperatures)
        assert result == [], f"Expected [] for: {reason}"



    @pytest.mark.parametrize("peak_value, position", [
        (10, 1), (25, 2), (50, 5), (99, 10), (200, 15)
    ])
    def test_peak_finder_single_injected_peak(self, peak_value, position):
      
        temps = list(range(position + 1))           
        temps[position] = peak_value                 
        temps += list(range(position - 1, -1, -1))  
        result = peak_finder(temps)
        assert peak_value in result
        assert len(result) == 1

    @pytest.mark.parametrize("num_peaks, peak_value, valley_value", [
        (3, 10, 1),
        (5, 50, 0),
        (10, 100, -5),
        (20, 999, 1),
    ])
    def test_peak_finder_known_number_of_peaks(self, num_peaks, peak_value, valley_value):
   
        temps = []
        for _ in range(num_peaks):
            temps.extend([valley_value, peak_value])
        temps.append(valley_value)  

        result = peak_finder(temps)
        assert len(result) == num_peaks
        assert all(t == peak_value for t in result)

    @pytest.mark.parametrize("gap_size", [1, 2, 3, 5, 10])
    def test_peak_finder_peaks_separated_by_gaps(self, gap_size):
        num_peaks = 5
        peak_val = 100
        valley_val = 1
        temps = [valley_val]
        for _ in range(num_peaks):
            temps.append(peak_val)
            temps.extend([valley_val] * gap_size)

        result = peak_finder(temps)
        assert len(result) == num_peaks
        assert all(t == peak_val for t in result)

    def test_peak_finder_order_preserved(self):
        temps = [1, 9, 1, 3, 1, 7, 1, 5, 1]
        result = peak_finder(temps)
        assert result == [9, 3, 7, 5]  

    def test_peak_finder_large_scale_zigzag(self):
        temps = ([1, 10] * 500) + [1]
        result = peak_finder(temps)
        assert len(result) == 500
        assert all(t == 10 for t in result)

    def test_peak_finder_large_scale_no_peaks(self):
        temps = list(range(10000))
        assert peak_finder(temps) == []



    def test_peak_finder_returns_list(self):
        assert isinstance(peak_finder([1, 2, 1]), list)

    def test_peak_finder_returns_list_on_empty(self):
        result = peak_finder([])
        assert result == []
        assert isinstance(result, list)

    def test_peak_finder_immutability(self):
        original = [30, 32, 31, 35, 33]
        copy = original.copy()
        peak_finder(original)
        assert original == copy, "Input list was mutated!"


    ################### Question 4 #########################
    @pytest.mark.parametrize("records, expected", [
        ([], {}),

        (
            [{"incident_id": "ESK-001", "area": "Soweto", "municipality": "CoJ", "province": "Gauteng",
              "stage": 2, "duration_hours": 2.5, "date": "2024-06-01", "start_time": "06:00",
              "end_time": "08:30", "status": "resolved", "scheduled": True, "affected_customers": 14200}],
            {"Stage 2": 2.5}
        ),

        (
            [
                {"incident_id": "ESK-001", "area": "Soweto",  "municipality": "CoJ", "province": "Gauteng",
                 "stage": 2, "duration_hours": 2.5, "date": "2024-06-01", "start_time": "06:00",
                 "end_time": "08:30", "status": "resolved", "scheduled": True, "affected_customers": 14200},
                {"incident_id": "ESK-002", "area": "Sandton", "municipality": "CoJ", "province": "Gauteng",
                 "stage": 2, "duration_hours": 1.5, "date": "2024-06-02", "start_time": "09:00",
                 "end_time": "10:30", "status": "resolved", "scheduled": True, "affected_customers": 8750},
            ],
            {"Stage 2": 4.0}
        ),

        (
            [
                {"incident_id": "ESK-001", "area": "Soweto",  "municipality": "CoJ", "province": "Gauteng",
                 "stage": 2, "duration_hours": 2.5, "date": "2024-06-01", "start_time": "06:00",
                 "end_time": "08:30", "status": "resolved", "scheduled": True, "affected_customers": 14200},
                {"incident_id": "ESK-002", "area": "Sandton", "municipality": "CoJ", "province": "Gauteng",
                 "stage": 4, "duration_hours": 4.0, "date": "2024-06-01", "start_time": "08:00",
                 "end_time": "12:00", "status": "resolved", "scheduled": True, "affected_customers": 8750},
            ],
            {"Stage 2": 2.5, "Stage 4": 4.0}
        ),

        (
            [
                {"incident_id": f"ESK-00{i}", "area": f"Area {i}", "municipality": "CoJ", "province": "Gauteng",
                 "stage": 1, "duration_hours": 2.0, "date": f"2024-06-0{i}", "start_time": "06:00",
                 "end_time": "08:00", "status": "resolved", "scheduled": True, "affected_customers": 5000}
                for i in range(1, 4)
            ],
            {"Stage 1": 6.0}
        ),

        (
            [
                {"incident_id": "ESK-001", "area": "Bellville",      "municipality": "CoCT", "province": "Western Cape",
                 "stage": 1, "duration_hours": 1.0, "date": "2024-06-01", "start_time": "09:00",
                 "end_time": "10:00", "status": "resolved", "scheduled": True, "affected_customers": 3200},
                {"incident_id": "ESK-002", "area": "Khayelitsha",     "municipality": "CoCT", "province": "Western Cape",
                 "stage": 2, "duration_hours": 2.0, "date": "2024-06-01", "start_time": "10:00",
                 "end_time": "12:00", "status": "resolved", "scheduled": True, "affected_customers": 29500},
                {"incident_id": "ESK-003", "area": "Mitchells Plain", "municipality": "CoCT", "province": "Western Cape",
                 "stage": 3, "duration_hours": 3.0, "date": "2024-06-01", "start_time": "13:00",
                 "end_time": "16:00", "status": "resolved", "scheduled": False, "affected_customers": 21000},
            ],
            {"Stage 1": 1.0, "Stage 2": 2.0, "Stage 3": 3.0}
        ),

        (
            [
                {"incident_id": "ESK-001", "area": "Centurion", "municipality": "CoT", "province": "Gauteng",
                 "stage": 6, "duration_hours": 5.0, "date": "2024-06-03", "start_time": "10:00",
                 "end_time": "15:00", "status": "resolved", "scheduled": True, "affected_customers": 33000},
                {"incident_id": "ESK-002", "area": "Germiston",  "municipality": "Ekurhuleni", "province": "Gauteng",
                 "stage": 6, "duration_hours": 3.0, "date": "2024-06-03", "start_time": "13:00",
                 "end_time": "16:00", "status": "resolved", "scheduled": True, "affected_customers": 11200},
            ],
            {"Stage 6": 8.0}
        ),

        (
            [
                {"incident_id": "ESK-001", "area": "Soweto",  "municipality": "CoJ", "province": "Gauteng",
                 "stage": 2, "duration_hours": 1.1, "date": "2024-06-01", "start_time": "06:00",
                 "end_time": "07:06", "status": "resolved", "scheduled": True, "affected_customers": 5000},
                {"incident_id": "ESK-002", "area": "Sandton", "municipality": "CoJ", "province": "Gauteng",
                 "stage": 2, "duration_hours": 2.2, "date": "2024-06-02", "start_time": "08:00",
                 "end_time": "10:12", "status": "resolved", "scheduled": True, "affected_customers": 5000},
            ],
            {"Stage 2": 3.3}
        ),
    ])
    def test_stage_summary_logic(self, records, expected):
        assert stage_summary(records) == expected



    def _make_record(self, i, stage, duration_hours):
        """Helper to build a realistic full record."""
        return {
            "incident_id": f"ESK-{i:05d}",
            "area": f"Area {i}",
            "municipality": "City of Johannesburg",
            "province": "Gauteng",
            "stage": stage,
            "duration_hours": duration_hours,
            "date": f"2024-06-{(i % 28) + 1:02d}",
            "start_time": "06:00",
            "end_time": "08:00",
            "status": "resolved",
            "scheduled": True,
            "affected_customers": 5000 + i
        }

    @pytest.mark.parametrize("stage, num_records, hours_each", [
        (1,  5,  2.0),
        (2, 10,  1.5),
        (3,  3,  4.0),
        (4,  7,  0.5),
        (6, 20,  3.0),
    ])
    def test_stage_summary_single_stage_computed_total(self, stage, num_records, hours_each):
        records = [self._make_record(i, stage, hours_each) for i in range(num_records)]
        expected_total = round(num_records * hours_each, 2)
        result = stage_summary(records)

        assert f"Stage {stage}" in result
        assert result[f"Stage {stage}"] == expected_total
        assert len(result) == 1  


    @pytest.mark.parametrize("stage_config", [
        {1: (5,  2.0), 2: (3,  1.5)},
        {2: (4,  3.0), 4: (6,  2.5), 6: (2,  5.0)},
        {1: (1,  1.0), 2: (2,  2.0), 3: (3,  3.0), 4: (4, 4.0)},
        {3: (10, 0.5), 6: (10, 0.5)},
        {1: (8,  1.25), 2: (5, 2.75), 3: (3, 0.5), 4: (7, 1.0), 6: (4, 3.5)},
    ])
    def test_stage_summary_multi_stage_computed_totals(self, stage_config):
        records = []
        idx = 0
        for stage, (count, hours) in stage_config.items():
            for _ in range(count):
                records.append(self._make_record(idx, stage, hours))
                idx += 1

        result = stage_summary(records)

        assert len(result) == len(stage_config)
        for stage, (count, hours) in stage_config.items():
            key = f"Stage {stage}"
            expected = round(count * hours, 2)
            assert key in result, f"{key} missing from result"
            assert result[key] == expected, f"{key}: expected {expected}, got {result[key]}"




    def test_stage_summary_no_phantom_stages(self):
        records = [
            self._make_record(0, 2, 2.0),
            self._make_record(1, 4, 3.0),
        ]
        result = stage_summary(records)
        assert set(result.keys()) == {"Stage 2", "Stage 4"}


    def test_stage_summary_large_scale(self):
        stages = [1, 2, 3, 4]
        hours_each = 2.0
        records = [self._make_record(i, stages[i % 4], hours_each) for i in range(1000)]
        result = stage_summary(records)

        assert len(result) == 4
        for stage in stages:
            expected = round(250 * hours_each, 2)
            assert result[f"Stage {stage}"] == expected


    def test_stage_summary_loaded_from_json(self):
        with open("loadshedding.json", "r") as f:
            records = json.load(f)

        result = stage_summary(records)

        expected = {}
        for record in records:
            key = f"Stage {record['stage']}"
            expected[key] = round(expected.get(key, 0) + record['duration_hours'], 2)

        assert isinstance(result, dict)
        assert all(k.startswith("Stage ") for k in result.keys())
        assert result == expected



    def test_stage_summary_returns_dict(self):
        result = stage_summary([self._make_record(0, 2, 2.0)])
        assert isinstance(result, dict)

    def test_stage_summary_empty_returns_dict(self):
        result = stage_summary([])
        assert result == {}
        assert isinstance(result, dict)

    def test_stage_summary_values_are_numeric(self):
        result = stage_summary([self._make_record(0, 2, 2.0)])
        for val in result.values():
            assert isinstance(val, (int, float)), f"Expected numeric, got {type(val)}"

    def test_stage_summary_immutability(self):
        records = [
            self._make_record(0, 2, 2.5),
            self._make_record(1, 4, 4.0),
        ]
        original = copy.deepcopy(records)
        stage_summary(records)
        assert records == original, "Input was mutated!"

    
    @pytest.mark.parametrize("height, expected", [
        (1, ["*"]),
        (2, [" *", "***"]),
        (3, ["  *", " * *", "*****"]),
        (4, ["   *", "  * *", " *   *", "*******"]),
        (5, ["    *", "   * *", "  *   *", " *     *", "*********"]),
    ])
    def test_draw_triangle_logic(self, height, expected):
        assert draw_triangle(height) == expected


    @pytest.mark.parametrize("height", [1, 2, 3, 5, 8, 10, 15, 20, 50])
    def test_draw_triangle_returns_correct_number_of_rows(self, height):
        result = draw_triangle(height)
        assert len(result) == height


    @pytest.mark.parametrize("height", [2, 3, 5, 8, 10, 15, 20])
    def test_draw_triangle_first_row_has_one_star(self, height):
        result = draw_triangle(height)
        assert result[0].strip() == "*"


    @pytest.mark.parametrize("height", [2, 3, 5, 8, 10, 15, 20])
    def test_draw_triangle_last_row_is_solid(self, height):
        """Last row must be all stars, width = 2*height-1."""
        result = draw_triangle(height)
        expected_width = 2 * height - 1
        assert result[-1].strip() == "*" * expected_width, \
            f"Last row should be {'*' * expected_width} for height {height}"


    @pytest.mark.parametrize("height", [3, 5, 8, 10, 15, 20])
    def test_draw_triangle_middle_rows_have_two_stars(self, height):
        """Every row except first and last must contain exactly 2 stars."""
        result = draw_triangle(height)
        for i, row in enumerate(result[1:-1], start=2):
            star_count = row.count("*")
            assert star_count == 2, \
                f"Row {i} of height {height} should have 2 stars, got {star_count}: '{row}'"


    @pytest.mark.parametrize("height", [3, 5, 8, 10, 15, 20])
    def test_draw_triangle_middle_rows_inner_spaces(self, height):
        """Middle rows: inner gap between the two stars must be 2*row_number - 3."""
        result = draw_triangle(height)
        for i, row in enumerate(result[1:-1], start=2):
            inner = row.strip()                    # remove leading spaces
            expected_inner_spaces = 2 * i - 3
            expected_inner = "*" + " " * expected_inner_spaces + "*"
            assert inner == expected_inner, \
                f"Row {i} height={height}: expected '{expected_inner}', got '{inner}'"


    @pytest.mark.parametrize("height", [2, 3, 5, 8, 10, 20])
    def test_draw_triangle_leading_spaces_decrease(self, height):
        """Each row must have one fewer leading space than the row before it."""
        result = draw_triangle(height)
        for i in range(1, len(result)):
            prev_spaces = len(result[i - 1]) - len(result[i - 1].lstrip())
            curr_spaces = len(result[i]) - len(result[i].lstrip())
            assert curr_spaces == prev_spaces - 1, \
                f"height={height}, row {i}: leading spaces should decrease by 1"


    @pytest.mark.parametrize("height", [3, 5, 8, 10, 20])
    def test_draw_triangle_peak_is_centred(self, height):
        """First row must have exactly height-1 leading spaces."""
        result = draw_triangle(height)
        expected_leading = height - 1
        actual_leading = len(result[0]) - len(result[0].lstrip())
        assert actual_leading == expected_leading, \
            f"height={height}: peak should have {expected_leading} leading spaces, got {actual_leading}"


    @pytest.mark.parametrize("height", [1, 2, 3, 5, 10])
    def test_draw_triangle_returns_list_of_strings(self, height):
        result = draw_triangle(height)
        assert isinstance(result, list)
        for row in result:
            assert isinstance(row, str), f"Each row must be a string, got {type(row)}"


    @pytest.mark.parametrize("height", [1, 2, 3, 5, 10])
    def test_draw_triangle_rows_contain_only_valid_chars(self, height):
        """Rows must only contain '*' and ' '."""
        result = draw_triangle(height)
        for row in result:
            for char in row:
                assert char in ("*", " "), f"Invalid character '{char}' in row: '{row}'"